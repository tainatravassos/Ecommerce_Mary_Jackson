"""Testes unitários do app_MJ
"""

from django.test import TestCase, Client
from django.urls import reverse
from app_MJ.models import Cliente, Categoria, Produto, Carrinho, CarrinhoProduto


class ClienteModelTest(TestCase):
    """
    Test cases para o model Cliente
    """

    def setUp(self):
        Cliente.objects.create(
            nome_completo="John Doe",
            endereco="123 Main St",
            cidade="Anytown",
            estado="NY",
            telefone="123-456-7890",
            email="john.doe@example.com",
            senha="password123",
        )

    def test_creation(self):
        """Test da criação do model"""
        cliente = Cliente.objects.first()
        self.assertEqual(cliente.nome_completo, "John Doe")
        self.assertEqual(cliente.endereco, "123 Main St")
        self.assertEqual(cliente.cidade, "Anytown")
        self.assertEqual(cliente.estado, "NY")
        self.assertEqual(cliente.telefone, "123-456-7890")
        self.assertEqual(cliente.email, "john.doe@example.com")
        self.assertEqual(cliente.senha, "password123")

    def test_str_representation(self):
        """Test do metodo str da classe"""
        cliente = Cliente.objects.first()
        self.assertEqual(str(cliente), cliente.nome_completo)


class CategoriaModelTest(TestCase):
    def setUp(self):
        Categoria.objects.create(nome="Electronics", slug="electronics")

    def test_creation(self):
        categoria = Categoria.objects.first()
        self.assertEqual(categoria.nome, "Electronics")
        self.assertEqual(categoria.slug, "electronics")

    def test_str_representation(self):
        categoria = Categoria.objects.first()
        self.assertEqual(str(categoria), categoria.nome)


class ProdutoModelTest(TestCase):
    def setUp(self):
        categoria = Categoria.objects.create(nome="Electronics", slug="electronics")
        Produto.objects.create(
            nome_produto="Smartphone",
            categoria=categoria,
            descricao="A high-quality smartphone.",
            quantidade=10,
            preco=99.99,
        )

    def test_creation(self):
        produto = Produto.objects.first()
        self.assertEqual(produto.nome_produto, "Smartphone")
        self.assertEqual(produto.categoria.nome, "Electronics")
        self.assertEqual(produto.descricao, "A high-quality smartphone.")
        self.assertEqual(produto.quantidade, 10)
        self.assertEqual(float(produto.preco), 99.99)

    def test_str_representation(self):
        produto = Produto.objects.first()
        self.assertEqual(str(produto), produto.nome_produto)


class CarrinhoModelTest(TestCase):
    def setUp(self):
        cliente = Cliente.objects.create(
            nome_completo="John Doe",
            endereco="123 Main St",
            cidade="Anytown",
            estado="NY",
            telefone="123-456-7890",
            email="john.doe@example.com",
            senha="password123",
        )
        Carrinho.objects.create(cliente=cliente)

    def test_creation(self):
        carrinho = Carrinho.objects.first()
        self.assertIsNotNone(carrinho.cliente)
        self.assertEqual(
            str(carrinho),
            f"Carrinho ID: {carrinho.id} - Cliente: {carrinho.cliente.nome_completo}",
        )


class CarrinhoProdutoModelTest(TestCase):
    def setUp(self):
        carrinho = Carrinho.objects.create()
        produto = Produto.objects.create(
            nome_produto="Smartphone",
            categoria=Categoria.objects.create(nome="Electronics", slug="electronics"),
            descricao="A high-quality smartphone.",
            quantidade=10,
            preco=99.99,
        )
        CarrinhoProduto.objects.create(
            carrinho=carrinho, produto=produto, quantidade=1, preco=99.99
        )

    def test_creation(self):
        carrinho_produto = CarrinhoProduto.objects.first()
        self.assertIsNotNone(carrinho_produto.carrinho)
        self.assertIsNotNone(carrinho_produto.produto)
        self.assertEqual(carrinho_produto.quantidade, 1)
        self.assertEqual(float(carrinho_produto.preco), 99.99)

    def test_str_representation(self):
        carrinho_produto = CarrinhoProduto.objects.first()
        self.assertEqual(
            str(carrinho_produto),
            f"Carrinho: {carrinho_produto.carrinho.id} - CarrinhoProduto: {carrinho_produto.id} - Produto: {carrinho_produto.produto.nome_produto}",
        )


class HomeViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.produto = Produto.objects.create(
            nome_produto="Smartphone",
            categoria=Categoria.objects.create(nome="Electronics", slug="electronics"),
            descricao="A high-quality smartphone.",
            quantidade=10,
            preco=99.99,
        )
        self.carrinho = Carrinho.objects.create()

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_lists_all_products(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTrue("produtos" in response.context)
        self.assertEqual(len(response.context["produtos"]), 1)
