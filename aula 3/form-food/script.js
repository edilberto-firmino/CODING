const formulario = document.getElementById("formPedido");

formulario.addEventListener("submit", function(event) {

    // Impede o formulário de recarregar a página
    event.preventDefault();

    // Pegando os dados do formulário
    const nome = document.getElementById("nome").value;
    const sabor = document.getElementById("sabor").value;
    const whatsapp = document.getElementById("whatsapp").value;
    const email = document.getElementById("email").value;
    const endereco = document.getElementById("endereco").value;
    const numero = document.getElementById("numero").value;

    const pizza = document.getElementById("pizza").value;
    const recheio = document.getElementById("recheio").value;
    const bordas = document.getElementById("bordas").value;
    const quantidade = document.getElementById("quantidade").value;


    // Remove espaços, parênteses e traços do telefone
    let telefone = whatsapp.replace(/\D/g, "");


    // Adiciona o código do Brasil
    // caso o usuário não tenha digitado
    if (!telefone.startsWith("55")) {
        telefone = "55" + telefone;
    }


    // Montando a mensagem do pedido
    const mensagem = `
🍕 *NOVO PEDIDO*

👤 *Cliente:* ${nome}

🍕 *Pizza:* ${pizza}
🥘 *Sabor:* ${sabor}
🧀 *Recheio:* ${recheio}
⭕ *Bordas:* ${bordas}
🔢 *Quantidade:* ${quantidade}

📍 *Endereço:* ${endereco}, ${numero}

📱 *WhatsApp:* ${whatsapp}
📧 *E-mail:* ${email}
    `;


    // Codifica a mensagem para funcionar na URL
    const mensagemCodificada = encodeURIComponent(mensagem);


    // Cria o link do WhatsApp
    const linkWhatsapp =
        `https://wa.me/${telefone}?text=${mensagemCodificada}`;


    // Redireciona para o WhatsApp
    window.location.href = linkWhatsapp;

});