#!/bin/bash

# Diretório do repositório Git
REPO_DIR="/home/tw/Desktop/Faculdade"

# Mensagem de commit padrão
COMMIT_MESSAGE="Auto-commit: $(date +'%Y-%m-%d %H:%M:%S')"

# Intervalo entre as verificações (em segundos)
INTERVALO=60

# Função para realizar git pull, commit e push
sync_repo() {
    cd $REPO_DIR

    # Verifica se há mudanças locais não comitadas
    if [[ -n $(git status -s) ]]; then
        echo "Mudanças locais detectadas. Fazendo commit e push..."
        git add .
        git commit -m "$COMMIT_MESSAGE"
    fi

    # Verifica se há mudanças no repositório remoto
    git fetch

    LOCAL=$(git rev-parse @)
    REMOTE=$(git rev-parse @{u})
    BASE=$(git merge-base @ @{u})

    if [ $LOCAL = $REMOTE ]; then
        echo "Repositório já está atualizado."

    elif [ $LOCAL = $BASE ]; then
        echo "Mudanças detectadas no remoto. Fazendo pull..."
        git pull --rebase

    elif [ $REMOTE = $BASE ]; then
        echo "Mudanças locais detectadas. Fazendo push..."
        git push

    else
        echo "Conflito detectado. Tentando resolver automaticamente..."
        git add .
        git commit -m "Auto-commit antes do merge: $(date +'%Y-%m-%d %H:%M:%S')"
        git pull --rebase || {
            echo "Conflito não resolvido automaticamente. Necessária intervenção manual."
            exit 1
        }
        git push
    fi
}

# Monitoramento contínuo
while true; do
    sync_repo
    sleep $INTERVALO
done