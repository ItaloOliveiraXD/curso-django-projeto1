from django.urls import resolve, reverse
from recipes import views
from .test_base_recipe import RecipeTestBase


class RecipesViewsTest(RecipeTestBase):
    def test_recipes_home_view_function_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)

    def test_recipes_home_view_returns_status_code_200_ok(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)

    def test_recipes_home_loads_correct_template(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

    def test_recipes_home_template_show_no_recipes_found_is_no_recipes(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertIn(
            '<h1>No recipes found here 😢</h1>',
            response.content.decode('utf-8')
        )

    def test_recipes_home_template_load_recipes(self):

        self.make_recipe()
        response = self.client.get(reverse('recipes:home'))
        context = response.context['recipes']
        content = response.content.decode('utf-8')

        self.assertEqual(len(context), 1)
        self.assertIn('Recipe title', content)

    def test_recipes_home_template_not_load_if_is_published_false(self):

        self.make_recipe(is_published=False)
        response = self.client.get(reverse('recipes:home'))
        content = response.content.decode('utf-8')

        self.assertIn(
            '<h1>No recipes found here 😢</h1>',
            content
        )

    def test_recipes_category_view_function_is_correct(self):
        view = resolve(reverse('recipes:category', kwargs={'category_id': 1}))
        self.assertIs(view.func, views.category)

    def test_recipes_category_view_returns_status_code_200_ok(self):

        self.make_recipe()
        response = self.client.get(
            reverse('recipes:category', kwargs={'category_id': 1})
        )
        self.assertEqual(response.status_code, 200)

    def test_recipes_category_view_returns_404_if_no_recipes_found(self):
        response = self.client.get(
            reverse('recipes:category', kwargs={'category_id': 1000})
        )
        self.assertEqual(response.status_code, 404)

    def test_recipes_category_template_load_recipes_the_category(self):
        title = 'this is title the category test'

        self.make_recipe(title=title)

        response = self.client.get(reverse('recipes:category', kwargs={'category_id': 1}))  # noqa: E501
        content = response.content.decode('utf-8')

        self.assertIn(title, content)

    def test_recipes_category_template_not_load_if_is_published_false(self):

        self.make_recipe(is_published=False)
        response = self.client.get(reverse('recipes:category', kwargs={'category_id': 1}))  # noqa: E501

        self.assertEqual(response.status_code, 404)

    def test_recipes_recipe_view_function_is_correct(self):
        view = resolve(reverse('recipes:recipe', kwargs={'id': 1}))
        self.assertIs(view.func, views.recipe)

    def test_recipes_recipe_view_returns_status_code_200_ok(self):

        self.make_recipe()
        response = self.client.get(
            reverse('recipes:recipe', kwargs={'id': 1})
        )
        self.assertEqual(response.status_code, 200)

    def test_recipes_recipe_view_returns_404_if_no_recipes_found(self):
        response = self.client.get(
            reverse('recipes:recipe', kwargs={'id': 1000})
        )
        self.assertEqual(response.status_code, 404)

    def test_recipes_recipe_template_load_one_recipe_correct(self):
        title = 'this is the title of the recipe details'

        self.make_recipe(title=title)

        response = self.client.get(reverse('recipes:recipe', kwargs={'id': 1}))
        content = response.content.decode('utf-8')

        self.assertIn(title, content)

    def test_recipes_recipe_template_not_load_if_is_published_false(self):

        recipe = self.make_recipe(is_published=False)
        response = self.client.get(reverse('recipes:recipe', kwargs={'id': recipe.id}))  # noqa: E501

        self.assertEqual(response.status_code, 404)
