from .test_base_recipe import RecipeTestBase, Recipe
from django.core.exceptions import ValidationError
from parameterized import parameterized


class RecipeModelsTest(RecipeTestBase):
    def setUp(self) -> None:
        self.recipe = self.make_recipe()
        return super().setUp()

    def make_recipe_with_default(self):
        recipe = Recipe(
            category=self.make_category(name='Essa é uma nova categoria'),
            author=self.make_author(username='newauthor'),
            title='Recipe title',
            description='Recipe description',
            slug='recipe-slug',
            preparation_time=10,
            preparation_time_unit='Minutos',
            servings=5,
            servings_unit='Porções',
            preparation_steps='Recipe preparation_steps',
        )

        recipe.full_clean()
        recipe.save()

        return recipe

    @parameterized.expand([
        ('title', 65),
        ('description', 165),
        ('preparation_time_unit', 165),
        ('servings_unit', 165),
    ]
    )
    def test_recipe_fields_max_length(self, field, max_length):
        setattr(self.recipe, field, 'A' * (max_length + 1))
        with self.assertRaises(ValidationError):
            self.recipe.full_clean()

    def test_recipe_preparation_steps_is_html_is_false_by_default(self):
        recipe = self.make_recipe_with_default()
        self.assertFalse(
            recipe.preparation_steps_is_html,
            msg='preparation_steps_is_html tem que ser por padrão False.',
        )

    def test_recipe_is_published_is_false_by_default(self):
        recipe = self.make_recipe_with_default()
        self.assertFalse(
            recipe.is_published,
            msg='is_published tem que ser por padrão False.',
        )

    def test_recipe_string_representation(self):
        newtitle = 'new title'
        self.recipe.title = newtitle
        self.recipe.full_clean()
        self.recipe.save()

        self.assertEqual(str(self.recipe), newtitle)
