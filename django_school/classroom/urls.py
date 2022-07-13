from django.urls import include, path
from .views import classroom, students, teachers, parents
from .views.students import Updateprofile

urlpatterns = [
    path('', classroom.home, name='home'),
    path('students/', include(([
        path('', students.QuizListView.as_view(), name='quiz_list'),
        path('s/', students.StudentList.as_view(), name='student_list'),
        path('interests/', students.StudentInterestsView.as_view(), name='student_interests'),
        path('taken/', students.TakenQuizListView.as_view(), name='taken_quiz_list'),
        path('quiz/<int:pk>/', students.take_quiz, name='take_quiz'),
        path('quiz/<int:pk>/studentresults/', students.QuizResultsView.as_view(), name='student_quiz_results'),
        path('xogame/', students.GameView.as_view(), name='xogame'),
        path('profile/', Updateprofile, name='profile'),
    ], 'classroom'), namespace='students')),

    path('teachers/', include(([
        path('', teachers.QuizListView.as_view(), name='quiz_change_list'),
        path('calendar/', teachers.CalendarView.as_view(), name='calendar'),
        path('quiz/add/', teachers.QuizCreateView.as_view(), name='quiz_add'),
        path('quiz/<int:pk>/', teachers.QuizUpdateView.as_view(), name='quiz_change'),
        path('quiz/<int:pk>/delete/', teachers.QuizDeleteView.as_view(), name='quiz_delete'),
        path('quiz/<int:pk>/results/', teachers.QuizResultsView.as_view(), name='quiz_results'),
        path('quiz/<int:pk>/question/add/', teachers.question_add, name='question_add'),
        path('quiz/<int:quiz_pk>/question/<int:question_pk>/', teachers.question_change, name='question_change'),
        path('quiz/<int:quiz_pk>/question/<int:question_pk>/delete/', teachers.QuestionDeleteView.as_view(), name='question_delete'),
    ], 'classroom'), namespace='teachers')),

    path('parents/', include(([
     path('', parents.QuizListView.as_view(), name='quiz_change_list'),
     path('quiz/<int:pk>/results/', parents.QuizResultsView.as_view(),name='quiz_results'),
     ], 'classroom'), namespace='parents')),
]
