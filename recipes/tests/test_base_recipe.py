from django.test import TestCase
from recipes.models import Category, Recipe, User


class RecipeTestBase(TestCase):

    def setUp(self) -> None:
        return super().setUp()

    def make_category(self, name='category'):
        return Category.objects.create(name=name)

    def make_author(
        self,
        first_name='user',
        last_name='name',
        username='username',
        password='123456',
        email='username@email.com',
    ):

        return User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=username,
                password=password,
                email=email,
            )

    def make_recipe(
        self,
        category_date=None,
        author_date=None,
        title='Recipe title',
        description='Recipe description',
        slug='recipe-slug',
        preparation_time=10,
        preparation_time_unit='Minutos',
        servings=5,
        servings_unit='Porções',
        preparation_steps='Recipe preparation_steps',
        preparation_steps_is_html=False,
        is_published=True,
    ):

        if category_date is None:
            category_date = {}

        if author_date is None:
            author_date = {}

        return Recipe.objects.create(
            category=self.make_category(**category_date),
            author=self.make_author(**author_date),
            title=title,
            description=description,
            slug=slug,
            preparation_time=preparation_time,
            preparation_time_unit=preparation_time_unit,
            servings=servings,
            servings_unit=servings_unit,
            preparation_steps=preparation_steps,
            preparation_steps_is_html=preparation_steps_is_html,
            is_published=is_published,
        )
