from .test_base_recipe import RecipeTestBase
from django.core.exceptions import ValidationError


class CategoryModelsTest(RecipeTestBase):
    def setUp(self) -> None:
        self.category = self.make_category(
            name='Category testing'
        )
        return super().setUp()

    def test_recipe_category_model_representation_string_is_name_field(self):
        self.assertEqual(str(self.category), self.category.name)

    def test_recipe_category_model_name_is_65_chars(self):
        newname = 'A' * 70
        self.category.name = newname

        with self.assertRaises(ValidationError):
            self.category.full_clean()
