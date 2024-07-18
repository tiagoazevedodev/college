#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Produto {
    char nome[30]; /* Nome do produto */
    int codigo;    /* Codigo do produto */
    double preco;  /* Preco do produto */
} Produto;

typedef struct node {
    Produto produto;
    struct node* next;
} Node;

void adicionarProduto(Node** head) {
    Node* novo = (Node*)malloc(sizeof(Node));
    if (novo == NULL) {
        printf("Erro de alocacao de memoria.\n");
        return;
    }
    printf("Digite o nome do produto: ");
    scanf("%s", novo->produto.nome);
    printf("Digite o codigo do produto: ");
    scanf("%d", &novo->produto.codigo);
    printf("Digite o preco do produto: ");
    scanf("%lf", &novo->produto.preco);
    novo->next = *head;
    *head = novo;
}

void exibirProdutos(Node* head) {
    Node* atual = head;
    while (atual != NULL) {
        printf("Nome: %s, Codigo: %d, Preco: %.2f\n",
               atual->produto.nome, atual->produto.codigo, atual->produto.preco);
        atual = atual->next;
    }
}

void buscarProduto(Node* head) {
    char nome[30];
    printf("Digite o nome do produto: ");
    scanf("%s", nome);
    Node* atual = head;
    while (atual != NULL) {
        if (strcmp(atual->produto.nome, nome) == 0) {
            printf("Nome: %s, Codigo: %d, Preco: %.2f\n",
                   atual->produto.nome, atual->produto.codigo, atual->produto.preco);
            return;
        }
        atual = atual->next;
    }
    printf("Produto nao encontrado.\n");
}

void liberarMemoria(Node* head) {
    Node* atual = head;
    while (atual != NULL) {
        Node* temp = atual;
        atual = atual->next;
        free(temp);
    }
}

int main() {
    Node* head = NULL;
    int opcao;

    do {
        printf("\nMenu:\n");
        printf("1. Adicionar produto\n");
        printf("2. Exibir todos os produtos\n");
        printf("3. Buscar produto por nome\n");
        printf("4. Sair\n");
        printf("Escolha uma opcao: ");
        scanf("%d", &opcao);

        switch (opcao) {
            case 1:
                adicionarProduto(&head);
                break;
            case 2:
                exibirProdutos(head);
                break;
            case 3:
                buscarProduto(head);
                break;
            case 4:
                liberarMemoria(head);
                printf("Saindo...\n");
                break;
            default:
                printf("Opcao invalida.\n");
        }
    } while (opcao != 4);

    return 0;
}
