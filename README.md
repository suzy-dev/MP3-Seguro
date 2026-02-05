# 🎵 MP3 Seguro – Downloader de Áudio

O **MP3 Seguro** é uma ferramenta simples e eficiente para converter vídeos do YouTube em arquivos MP3 de alta qualidade diretamente para o seu computador ou pendrive.

✔ Seguro  
✔ Portátil  
✔ Fácil de usar  

---

## 🚀 Como usar

Você **não precisa instalar Python** nem configurar nada complicado.

1. **Baixe o programa**  
   Vá até a seção **Releases** e baixe o arquivo `MP3_Seguro_v1.0.zip`.

2. **Extraia os arquivos**  
   Clique com o botão direito no arquivo baixado e escolha **“Extrair Tudo”**.

   ⚠️ **Importante:** mantenha todos os arquivos da pasta juntos para o programa funcionar corretamente.

3. **Abra o aplicativo**  
   Dê um duplo clique em `MP3_Seguro.exe`.

4. **Baixe sua música**
   - Cole o link do vídeo do YouTube  
   - Clique em **Escolher Pasta** (caso queira salvar direto no pendrive)  
   - Clique em **BAIXAR EM MP3** e aguarde a barra de progresso  

---

## ✨ Diferenciais Técnicos

- **Interface moderna**  
  Desenvolvida com **CustomTkinter**, incluindo suporte a *Dark Mode*.

- **Multithreading**  
  O download acontece em segundo plano, evitando travamentos da interface.

- **Portabilidade total**  
  O software é distribuído com os binários necessários (**yt-dlp** e **ffmpeg**) integrados.

- **Caminhos dinâmicos**  
  Permite execução a partir de pendrives ou pastas externas sem necessidade de instalação.

- **Tratamento de dados**  
  Limpeza inteligente de URLs para evitar erros causados por playlists ou parâmetros extras.

---

## 📂 Estrutura do Pacote

Ao baixar a versão pronta, você encontrará:

- `MP3_Seguro.exe` — Interface gráfica do usuário  
- `yt-dlp.exe` — Responsável por buscar o conteúdo no YouTube  
- `ffmpeg.exe` — Conversão de vídeo para áudio MP3  
---

## 🔐 Segurança e Integridade

Para garantir a transparência e a segurança dos usuários, este projeto adota práticas recomendadas de distribuição de software:

### 1. Verificação de Integridade (Checksum)
Você pode confirmar que o arquivo baixado é exatamente o original gerado pela desenvolvedora e que não foi corrompido ou alterado por terceiros conferindo sua "impressão digital" (Hash SHA-256).

**Hash SHA-256 Oficial:**
`B27E0893AC69A260A64B5E13D1831B5EEA85500AD23977FDC4A46F4601081BB1`

**Como verificar no Windows (PowerShell):**
```powershell
Get-FileHash .\MP3_Seguro_v1.0.zip

---

## 📌 Observações

- Projeto desenvolvido com fins **educacionais e de aprendizado técnico**.
- Criado para **uso pessoal**, sem fins comerciais.
- O autor não se responsabiliza pelo uso indevido da ferramenta.
- Recomenda-se utilizar apenas com conteúdos de **direito próprio ou autorizados**.
- Respeite os termos de uso do YouTube e a legislação vigente de direitos autorais.

