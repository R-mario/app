import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Pregunta

# Create your tests here.

class ModeloPreguntaTests(TestCase):

    def publica_pregunta(self,delta):
        """
        función general para crear un objeto Pregunta y llamar a la función
        publicada_recientemente

        Returns:
            bool
        """

        tiempo = timezone.now() + datetime.timedelta(days=delta)

        return Pregunta(fecha_pub=tiempo).publicada_recientemente()

    def test_publicada_recientemente_a_futuro(self):
        """
        publicada_recientemente()
        debe devolver FALSO si la pregunta ocurre en el futuro
        """
        pregunta = self.publica_pregunta(-2)
        self.assertFalse(pregunta)
    
    
    def test_publicada_recientemente_falso(self):
        """
        publicada_recientemente()
        debe devolver False cuando ocurre en más de un día anterior
        """
        pregunta = self.publica_pregunta(-10)
        self.assertFalse(pregunta)

    def test_publicada_recientemente_cierto(self):
        """
        publicada_recientemente()
        debe devolver True si la pregunta ocurre en menos de un dia
        """
        tiempo = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        pregunta = Pregunta(fecha_pub=tiempo).publicada_recientemente()

        self.assertTrue(pregunta)

def crea_pregunta(pregunta,dias):
    """
    Crea una pregunta nueva dado los parámetros.
    Params:
        pregunta: pregunta_texto field
        dias: fecha_pub field
    Returns:
        Pregunta
    """
    time = timezone.now() + datetime.timedelta(days=dias)
    return Pregunta.objects.create(pregunta_texto=pregunta,
    fecha_pub=time)

class PreguntaIndexViewTest(TestCase):

    def test_0_preguntas(self):
        """ comprueba el mensaje de la respuesta cuando no hay preguntas """
        respuesta = self.client.get(reverse('encuestas:encuestas_indice'))
        self.assertEqual(respuesta.status_code,200) #200 = OK
        self.assertContains(respuesta, "No encuestas are available" )

        self.assertQuerysetEqual(respuesta.context['lista_preguntas'],[]) #???
    
    def test_pregunta_pasada(self):
        """
        Questions with a pub_date in the past are displayed on the
        index page.
        """
        question = crea_pregunta(pregunta="Past question.", dias=-30)
        response = self.client.get(reverse('encuestas:encuestas_indice'))
        self.assertQuerysetEqual(
            response.context['lista_preguntas'],
            [question],
        )

    def test_future_question(self):
        """
        Questions with a pub_date in the future aren't displayed on
        the index page.
        """
        crea_pregunta(pregunta="Future question.", dias=30)
        response = self.client.get(reverse('encuestas:encuestas_indice'))
        self.assertContains(response, '')
        self.assertQuerysetEqual(response.context['lista_preguntas'], [])

    def test_future_question_and_past_question(self):
        """
        Even if both past and future questions exist, only past questions
        are displayed.
        """
        question = crea_pregunta(pregunta="Past question.", dias=-30)
        crea_pregunta(pregunta="Future question.", dias=30)
        response = self.client.get(reverse('encuestas:encuestas_indice'))
        self.assertQuerysetEqual(
            response.context['lista_preguntas'],
            [question],
        )

    def test_two_past_questions(self):
        """
        The questions index page may display multiple questions.
        """
        question1 = crea_pregunta(pregunta="Past question 1.", dias=-30)
        question2 = crea_pregunta(pregunta="Past question 2.", dias=-5)
        response = self.client.get(reverse('encuestas:encuestas_indice'))
        self.assertQuerysetEqual(
            response.context['lista_preguntas'],
            [question2, question1],
        )

class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        """
        The detail view of a question with a pub_date in the future
        returns a 404 not found.
        """
        future_question = crea_pregunta(pregunta='Future question.', dias=5)
        url = reverse('encuestas:detalle', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        """
        The detail view of a question with a pub_date in the past
        displays the question's text.
        """
        past_question = crea_pregunta(pregunta='Past Question.', dias=-5)
        url = reverse('encuestas:detalle', args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.pregunta_texto)
