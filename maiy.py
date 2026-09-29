#include <iostream>
#include <string>
#include <limits>

using namespace std;

// Função para limpar o buffer de entrada
void limparBuffer() {
    cin.ignore(numeric_limits<streamsize>::max(), '\n');
}

// Exibe o cabeçalho do sistema
void mostrarCabecalho() {
    cout << "\n********************************\n";
    cout << "       BANCO INF101\n";
    cout << "********************************\n";
}

// Exibe os dados da conta
void consultarConta(
    int numeroConta,
    const string& nomeCliente,
    const string& cpf,
    int tipoConta,
    double saldo,
    bool contaAtiva
) {
    cout << "\n===== DADOS DA CONTA =====\n";

    cout << "Numero da conta: " << numeroConta << endl;
    cout << "Nome do titular: " << nomeCliente << endl;
    cout << "CPF: " << cpf << endl;

    cout << "Tipo da conta: ";

    if (tipoConta == 1) {
        cout << "Corrente";
    } else {
        cout << "Poupanca";
    }

    cout << endl;
    cout << "Saldo: R$ " << saldo << endl;

    cout << "Situacao: ";

    if (contaAtiva) {
        cout << "Ativa";
    } else {
        cout << "Inativa";
    }

    cout << endl;
}

// Verifica se uma conta foi cadastrada
bool contaExiste(int numeroConta) {
    return numeroConta > 0;
}

int main() {

    // =========================================================
    // VARIAVEIS OBRIGATORIAS
    // =========================================================

    int numeroConta = 0;
    string nomeCliente = "";
    string cpf = "";
    int tipoConta = 0;
    double saldo = 0.0;
    bool contaAtiva = false;

    // Controle do menu
    int opcao;

    mostrarCabecalho();

    do {

        cout << "\n========== MENU ==========\n";
        cout << "1 - Cadastrar conta\n";
        cout << "2 - Consultar conta\n";
        cout << "3 - Verificar saldo\n";
        cout << "4 - Alterar tipo da conta\n";
        cout << "5 - Ativar/Desativar conta\n";
        cout << "6 - Sair\n";
        cout << "==========================\n";
        cout << "Escolha uma opcao: ";

        cin >> opcao;

        // Verifica se a opção é realmente um número
        if (cin.fail()) {
            cin.clear();
            limparBuffer();

            cout << "\nEntrada invalida! Digite uma opcao de 1 a 6.\n";
            continue;
        }

        limparBuffer();

        switch (opcao) {

            // =================================================
            // 1 - CADASTRAR CONTA
            // =================================================
            case 1: {

                cout << "\n===== CADASTRO DE CONTA =====\n";

                // Número da conta
                do {
                    cout << "Numero da conta: ";
                    cin >> numeroConta;

                    if (cin.fail()) {
                        cin.clear();
                        limparBuffer();
                        numeroConta = 0;
                        cout << "Digite um numero valido.\n";
                    } else if (numeroConta <= 0) {
                        cout << "O numero da conta deve ser maior que zero.\n";
                    }

                } while (numeroConta <= 0);

                limparBuffer();

                // Nome
                do {
                    cout << "Nome do titular: ";
                    getline(cin, nomeCliente);

                    if (nomeCliente.empty()) {
                        cout << "O nome nao pode ficar vazio.\n";
                    }

                } while (nomeCliente.empty());

                // CPF
                do {
                    cout << "CPF do titular: ";
                    getline(cin, cpf);

                    if (cpf.empty()) {
                        cout << "O CPF nao pode ficar vazio.\n";
                    }

                } while (cpf.empty());

                // Tipo da conta
                do {
                    cout << "\nTipo da conta:\n";
                    cout << "1 - Corrente\n";
                    cout << "2 - Poupanca\n";
                    cout << "Escolha: ";

                    cin >> tipoConta;

                    if (cin.fail()) {
                        cin.clear();
                        limparBuffer();
                        tipoConta = 0;
                        cout << "Digite apenas 1 ou 2.\n";
                    } else if (tipoConta != 1 && tipoConta != 2) {
                        cout << "O tipo da conta deve ser 1 ou 2.\n";
                    }

                } while (tipoConta != 1 && tipoConta != 2);

                // Saldo inicial
                do {
                    cout << "Saldo inicial: R$ ";
                    cin >> saldo;

                    if (cin.fail()) {
                        cin.clear();
                        limparBuffer();
                        saldo = -1;
                        cout << "Digite um valor numerico valido.\n";
                    } else if (saldo < 0) {
                        cout << "O saldo inicial nao pode ser negativo.\n";
                    }

                } while (saldo < 0);

                // Conta começa ativa
                contaAtiva = true;

                limparBuffer();

                cout << "\nConta cadastrada com sucesso!\n";

                break;
            }

            // =================================================
            // 2 - CONSULTAR CONTA
            // =================================================
            case 2: {

                if (!contaExiste(numeroConta)) {
                    cout << "\nNenhuma conta foi cadastrada ainda.\n";
                    break;
                }

                consultarConta(
                    numeroConta,
                    nomeCliente,
                    cpf,
                    tipoConta,
                    saldo,
                    contaAtiva
                );

                break;
            }

            // =================================================
            // 3 - VERIFICAR SALDO
            // =================================================
            case 3: {

                if (!contaExiste(numeroConta)) {
                    cout << "\nNenhuma conta foi cadastrada ainda.\n";
                    break;
                }

                cout << "\n===== SALDO =====\n";
                cout << "Conta: " << numeroConta << endl;
                cout << "Titular: " << nomeCliente << endl;
                cout << "Saldo atual: R$ " << saldo << endl;

                break;
            }

            // =================================================
            // 4 - ALTERAR TIPO DA CONTA
            // =================================================
            case 4: {

                if (!contaExiste(numeroConta)) {
                    cout << "\nNenhuma conta foi cadastrada ainda.\n";
                    break;
                }

                cout << "\n===== ALTERAR TIPO DA CONTA =====\n";

                cout << "Tipo atual: ";

                if (tipoConta == 1) {
                    cout << "Corrente\n";
                } else {
                    cout << "Poupanca\n";
                }

                do {
                    cout << "\nNovo tipo:\n";
                    cout << "1 - Corrente\n";
                    cout << "2 - Poupanca\n";
                    cout << "Escolha: ";

                    cin >> tipoConta;

                    if (cin.fail()) {
                        cin.clear();
                        limparBuffer();
                        tipoConta = 0;
                        cout << "Digite apenas 1 ou 2.\n";
                    } else if (tipoConta != 1 && tipoConta != 2) {
                        cout << "Opcao invalida.\n";
                    }

                } while (tipoConta != 1 && tipoConta != 2);

                limparBuffer();

                cout << "\nTipo da conta alterado com sucesso!\n";

                break;
            }

            // =================================================
            // 5 - ATIVAR/DESATIVAR CONTA
            // =================================================
            case 5: {

                if (!contaExiste(numeroConta)) {
                    cout << "\nNenhuma conta foi cadastrada ainda.\n";
                    break;
                }

                contaAtiva = !contaAtiva;

                cout << "\nConta ";

                if (contaAtiva) {
                    cout << "ativada";
                } else {
                    cout << "desativada";
                }

                cout << " com sucesso!\n";

                break;
            }

            // =================================================
            // 6 - SAIR
            // =================================================
            case 6:

                cout << "\nEncerrando o sistema...\n";
                cout << "Obrigado por utilizar o Banco INF101!\n";

                break;

            // =================================================
            // OPÇÃO INVÁLIDA
            // =================================================
            default:

                cout << "\nOpcao invalida! Escolha uma opcao de 1 a 6.\n";

                break;
        }

    } while (opcao != 6);

    return 0;
}
