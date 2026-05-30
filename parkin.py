import streamlit as st
from pathlib import Path

st.set_page_config(page_title="ParkinSense", page_icon="🩺", layout="wide")

BASE_DIR = Path(__file__).parent
IMAGE_DIR = BASE_DIR / "imagens"


def find_image(name):
    possible_names = [
        name,
        f"{name}.jpeg",
        f"{name}.jpg",
        f"{name}.png",
        f"{name}.webp",
        f"{name}.JPEG",
        f"{name}.JPG",
        f"{name}.PNG",
        f"{name}.WEBP",
    ]

    for possible_name in possible_names:
        img_path = IMAGE_DIR / possible_name
        if img_path.exists():
            return img_path

    return None


def show_image(name, caption=None, width=None):
    img_path = find_image(name)

    if img_path:
        if width:
            st.image(str(img_path), caption=caption, width=width)
        else:
            st.image(str(img_path), caption=caption, width="stretch")
    else:
        st.error(f"Imagem não encontrada: {IMAGE_DIR / name}")
        if IMAGE_DIR.exists():
            st.write("Ficheiros encontrados na pasta imagens:")
            st.write([p.name for p in IMAGE_DIR.iterdir()])
        else:
            st.write("A pasta imagens não existe.")


if "product_selected" not in st.session_state:
    st.session_state.product_selected = None


products = {
    "Luva de Estabilização": {
        "tagline": "Sistema inteligente de estabilização ativa desenvolvido para reduzir os efeitos dos tremores em tempo real.",
        "desc": "A Luva de Estabilização Ativa ParkinSense foi desenvolvida para reduzir os efeitos dos tremores através de um sistema de compensação inteligente em tempo real. Utilizando atuadores giroscópicos e algoritmos adaptativos, a luva aplica forças contrárias que ajudam a estabilizar os movimentos do utilizador durante tarefas do quotidiano.",
        "image_file": "luva",
        "tech_details": """
        ### 🧪 Especificações e Arquitetura Biomédica
        * **Têxteis e Estrutura:** Base em tecidos elásticos de Lycra ou Spandex para garantir que os sensores fiquem colados à pele sem restringir o movimento voluntário.
        * **Fios Condutores:** Uso de fios condutores de prata ou aço inoxidável costurados no próprio tecido.
        * **Módulo IMU:** MPU6050 posicionado no dorso da mão.
        """,
    },
    "Pulseira de Monitorização": {
        "tagline": "Wearable inteligente capaz de monitorizar padrões motores e recolher dados clínicos continuamente.",
        "desc": "A pulseira inteligente ParkinSense permite a recolha contínua de dados motores através de sensores inerciais de elevada precisão. Os dados são enviados para a aplicação móvel via Bluetooth, permitindo análise inteligente e acompanhamento clínico contínuo.",
        "image_file": "pulseira",
        "tech_details": """
        ### 📊 Engenharia de Sinais e Processamento
        * **Aquisição de Dados:** Sensores IMU captam movimentos lineares e rotativos.
        * **Processamento Local:** Filtragem digital e FFT para mapear a frequência dominante do tremor.
        * **Comunicação:** Transmissão via Bluetooth Low Energy.
        """,
    },
    "Pulseira Desportiva": {
        "tagline": "Solução wearable direcionada para monitorização de movimento e desempenho físico.",
        "desc": "Uma versão otimizada com bracelete de silicone biomédico e hipoalergénico. Conta com algoritmos adaptativos focados em isolar o ruído mecânico gerado pelas atividades de reabilitação física e exercícios moderados.",
        "image_file": "pulseira",
        "tech_details": "### 🏃 Reabilitação e Performance\nFiltros digitais dinâmicos ajustam-se ao movimento voluntário do utilizador, assegurando que o mapeamento clínico de tremores em repouso e em ação permaneça fidedigno mesmo durante o esforço físico.",
    },
    "Aplicação Premium": {
        "tagline": "Aplicação móvel com análise inteligente de dados clínicos, relatórios personalizados e monitorização remota.",
        "desc": "A aplicação ParkinSense funciona como centro inteligente do ecossistema, permitindo análise, visualização e armazenamento dos dados recolhidos. Através de algoritmos de inteligência artificial, a aplicação gera relatórios clínicos personalizados e facilita a comunicação entre paciente e profissional de saúde.",
        "image_file": None,
        "tech_details": "### 🧠 Ecossistema Cloud & Inteligência Artificial\nInterface voltada para a geração de dashboards intuitivos, transformando vetores cinemáticos crus em relatórios estruturados em PDF prontos a apresentar em consultas de neurologia.",
    },
}


st.sidebar.title("🩺 ParkinSense")
st.sidebar.caption("Healthcare Innovation for Better Living")
st.sidebar.markdown("---")

menu = st.sidebar.radio(
    "Navegação do Website",
    ["Página Inicial", "Produtos", "Como Funciona", "Sobre Nós", "Roadmap", "Contactos"],
)

st.sidebar.markdown("---")
st.sidebar.info(
    "📌 Lançamento Oficial: **2027**\n"
    "Licenciatura em Engenharia Biomédica\n"
    "**Universidade do Minho**"
)


if menu == "Página Inicial":
    logo_col, title_col = st.columns([1, 3])

    with logo_col:
        show_image("logo", width=220)

    with title_col:
        st.markdown(
            """
            <div style="height: 220px; display: flex; align-items: center;">
                <h1 style="font-size: 72px; margin: 0;">ParkinSense</h1>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("### Monitorização Inteligente e Estabilização Ativa para devolver a sua autonomia.")

    st.markdown("---")
    st.write("### 🖼️ Antevisão")

    col_mock1, col_mock2, col_mock3 = st.columns(3)

    # --- CÓDIGO ALTERADO ---
    with col_mock1:
        show_image("pulseira", caption="Pulseira de Monitorização")

    with col_mock2:
        # Ajustei o width para 250 para ficar mais pequena (pode alterar este número)
        show_image("luva", caption="Luva de Estabilização Ativa", width=250)

    with col_mock3:
        # Substituímos o aviso pela imagem real da app
        show_image("app", caption="Interface da Aplicação ParkinSense",width=150)
    # -----------------------

    st.markdown("---")

    st.header("🔬 Porque o Parkinson Precisa de uma Nova Abordagem")
    st.write(
        """
        A doença de Parkinson é uma das patologias neurodegenerativas mais prevalentes do mundo,
        afetando milhares de pessoas e comprometendo significativamente a sua qualidade de vida.

        Atualmente, o acompanhamento clínico depende maioritariamente de consultas pontuais e da
        descrição subjetiva dos sintomas por parte do paciente.

        O **ParkinSense** nasce para responder a estes desafios através de uma solução biomédica
        inteligente, acessível e orientada para o futuro da saúde digital.
        """
    )

    st.markdown("---")

    st.header("💡 Uma Plataforma Inteligente de Monitorização e Estabilização")
    p1, p2, p3 = st.columns(3)

    with p1:
        st.markdown("#### 🔗 Pilar 1 — Integração Inteligente")
        st.write("Monitorização contínua e estabilização ativa num único ecossistema tecnológico.")

    with p2:
        st.markdown("#### 🤖 Pilar 2 — IA Adaptativa")
        st.write("Algoritmos de IA analisam o padrão motor individual de cada utilizador.")

    with p3:
        st.markdown("#### 📊 Pilar 3 — Evidência Clínica")
        st.write("Dados convertidos em relatórios e dashboards clínicos.")


elif menu == "Produtos":
    if st.session_state.product_selected is None:
        st.title("Os Nossos Produtos")
        st.write(
            "A ParkinSense desenvolve soluções biomédicas inovadoras focadas na monitorização "
            "e estabilização de sintomas associados à doença de Parkinson."
        )

        st.info("📢 **Nota de Mercado:** Todos os produtos estarão oficialmente disponíveis em 2027.")

        st.markdown("---")

        cols = st.columns(2)

        for index, (prod_name, prod_info) in enumerate(products.items()):
            col = cols[index % 2]

            with col:
                st.subheader(prod_name)

                if prod_info["image_file"]:
                    show_image(prod_info["image_file"], width=400)
                else:
                    st.caption("🎨 *Design visual e mockup em fase de renderização.*")

                st.write(prod_info["tagline"])

                if st.button(f"Ver Especificações Técnicas ➔", key=f"nav_{prod_name}"):
                    st.session_state.product_selected = prod_name
                    st.rerun()

                st.markdown("---")

        st.markdown(
            """
            <div style="
                margin-top: 30px;
                padding: 28px;
                border-radius: 10px;
                background-color: rgba(80, 140, 255, 0.18);
                border: 1px solid rgba(120, 170, 255, 0.35);
                text-align: center;
            ">
                <h1 style="margin: 0;">Brevemente disponível — 2027</h1>
            </div>
            """,
            unsafe_allow_html=True,
        )

    else:
        current_prod = st.session_state.product_selected
        p_data = products[current_prod]

        if st.button("← Voltar à Exposição Geral"):
            st.session_state.product_selected = None
            st.rerun()

        st.markdown("---")
        st.title(current_prod)

        col_left, col_right = st.columns([1.2, 1])

        with col_left:
            st.subheader("Descrição")
            st.write(p_data["desc"])
            st.markdown(p_data["tech_details"])

        with col_right:
            if p_data["image_file"]:
                show_image(
                    p_data["image_file"],
                    caption=f"Conceito de Design Industrial - {current_prod}",
                )

            if "Luva" in current_prod:
                st.subheader("⚙️ Funcionalidades")
                for f in [
                    "Estabilização ativa do tremor",
                    "Resposta em tempo real",
                    "Tecnologia giroscópica inteligente",
                    "Design ergonómico",
                    "Integração com a aplicação móvel",
                ]:
                    st.write(f"• {f}")

                st.subheader("🎁 Benefícios")
                for b in [
                    "Maior autonomia",
                    "Melhoria da qualidade de vida",
                    "Redução da dificuldade em tarefas motoras",
                    "Apoio contínuo ao utilizador",
                ]:
                    st.write(f"• {b}")

            elif "Monitorização" in current_prod or "Desportiva" in current_prod:
                st.subheader("⚙️ Funcionalidades")
                for f in [
                    "Sensores IMU de alta precisão",
                    "Monitorização contínua",
                    "Conectividade Bluetooth",
                    "Recolha de padrões motores",
                    "Integração cloud",
                ]:
                    st.write(f"• {f}")

                st.subheader("🎁 Benefícios")
                for b in [
                    "Dados clínicos em tempo real",
                    "Monitorização remota",
                    "Apoio ao diagnóstico",
                    "Acompanhamento personalizado",
                ]:
                    st.write(f"• {b}")

            else:
                st.subheader("⚙️ Funcionalidades")
                st.write("• Filtros adaptativos dinâmicos inovadores.")
                st.write("• Exportação analítica automática.")
                st.subheader("🎁 Benefícios")
                st.write("• Apoio objetivo baseado em evidências de Engenharia Biomédica.")


elif menu == "Como Funciona":
    st.title("Como Funciona o ParkinSense")
    st.markdown("---")

    e1, e2, e3, e4 = st.columns(4)

    with e1:
        st.markdown("### 🛠️ Etapa 1\n**Recolha de Dados**")
        st.write("A pulseira inteligente monitoriza continuamente os movimentos.")

    with e2:
        st.markdown("### 🧠 Etapa 2\n**Análise Inteligente**")
        st.write("Os dados são enviados para a aplicação móvel e analisados por IA.")

    with e3:
        st.markdown("### ⚡ Etapa 3\n**Estabilização Ativa**")
        st.write("A luva ativa mecanismos giroscópicos para compensar os tremores.")

    with e4:
        st.markdown("### ☁️ Etapa 4\n**Plataforma Cloud**")
        st.write("O histórico fica disponível para monitorização clínica remota.")


elif menu == "Sobre Nós":
    st.title("Sobre a ParkinSense")
    st.write(
        """
        A ParkinSense é um projeto desenvolvido por estudantes de Engenharia Biomédica da
        **Universidade do Minho**.

        A nossa missão é desenvolver soluções inovadoras capazes de melhorar a qualidade de vida
        de pessoas com doença de Parkinson.
        """
    )

    st.markdown("---")
    st.header("👥 Equipa")

    team_cols = st.columns(4)
    names = ["Adriana MNonteiro", "Andreia Cardoso", "Catarina Marantes", "Elsa Peixoto"]

    for i, name in enumerate(names):
        with team_cols[i]:
            st.markdown(f"#### {name}")
            st.caption("Engenharia Biomédica")


elif menu == "Roadmap":
    st.title("Roadmap de Desenvolvimento")
    st.markdown("---")

    r1, r2 = st.columns(2)

    with r1:
        st.header("📅 2026")
        st.subheader("Desenvolvimento e Crescimento")
        st.write("• Arranque oficial do projeto;")
        st.write("• Desenvolvimento tecnológico;")
        st.write("• Construção dos protótipos;")
        st.write("• Captação de investimento.")

    with r2:
        st.header("📅 2027")
        st.subheader("Entrada no Mercado")
        st.write("• Lançamento oficial dos produtos;")
        st.write("• Expansão nacional;")
        st.write("• Consolidação da plataforma;")
        st.write("• Crescimento internacional.")


elif menu == "Contactos":
    st.title("Entre em Contacto")
    st.write(
        "Tem alguma questão, sugestão ou interesse em colaborar connosco? "
        "A nossa equipa está disponível para responder."
    )

    col_form, col_info = st.columns([1.5, 1])

    with col_form:
        with st.form(key="contacto_final"):
            nome = st.text_input("Nome")
            email = st.text_input("Email")

            tipo_cliente = st.selectbox(
                "Tipo de contacto / cliente (opcional)",
                [
                    "Prefiro não indicar",
                    "Paciente / Doente",
                    "Cuidador",
                    "Profissional médico",
                    "Clínica privada",
                    "Hospital",
                    "Instituição pública / SNS",
                    "Investidor / Parceiro",
                    "Outro",
                ],
            )

            mensagem = st.text_area("Mensagem")
            submitted = st.form_submit_button("Enviar")

            if submitted:
                if nome and email and mensagem:
                    st.success("Mensagem enviada com sucesso!")
                    st.info(f"Tipo de contacto selecionado: {tipo_cliente}")
                else:
                    st.error("Por favor, preencha nome, email e mensagem.")

    with col_info:
        st.subheader("Informações Adicionais")
        st.write("📧 **Email:** contacto@parkinsense.uminho.pt")
        st.write("🏫 **Instituição:** Universidade do Minho")
        st.write("🌐 **Redes Sociais & Professional:** LinkedIn")


st.markdown("---")

footer_col1, footer_col2 = st.columns([2, 1])

with footer_col1:
    st.caption("ParkinSense © 2026 | Healthcare Innovation for Better Living")

with footer_col2:
    st.caption(
        "Projeto desenvolvido no âmbito da Licenciatura em Engenharia Biomédica — Universidade do Minho."
    )
