import streamlit as st
from datetime import datetime
import streamlit.components.v1 as components


# =========================================================
# CONFIGURACIÓN DE LA APP
# =========================================================

st.set_page_config(
    page_title="Sistema de Soporte Técnico",
    page_icon="🛠️",
    layout="wide"
)



# =========================================================
# DISEÑO EMPRESARIAL — HTML + CSS + JS
# =========================================================

st.markdown("""
<style>
:root {
    --navy: #0B1220;
    --navy-2: #111C30;
    --blue: #2563EB;
    --blue-light: #60A5FA;
    --cyan: #22D3EE;
    --surface: #FFFFFF;
    --surface-2: #F5F7FB;
    --text: #172033;
    --muted: #64748B;
    --border: #E2E8F0;
}

.stApp {
    background:
        radial-gradient(circle at 15% 5%, rgba(37,99,235,.09), transparent 28%),
        radial-gradient(circle at 90% 10%, rgba(34,211,238,.07), transparent 25%),
        #F5F7FB;
    color: var(--text);
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0B1220 0%, #111C30 100%);
    border-right: 1px solid rgba(255,255,255,.08);
}

[data-testid="stSidebar"] * {
    color: #E8EEF8 !important;
}

[data-testid="stSidebar"] [data-testid="stRadio"] label {
    border-radius: 12px;
    padding: 9px 12px;
    transition: all .25s ease;
}

[data-testid="stSidebar"] [data-testid="stRadio"] label:hover {
    background: rgba(96,165,250,.13);
    transform: translateX(5px);
    box-shadow: 0 0 20px rgba(37,99,235,.15);
}

h1, h2, h3 {
    color: var(--navy) !important;
    letter-spacing: -.02em;
}

h1 {
    animation: slideDown .65s ease both;
}

.hero {
    position: relative;
    overflow: hidden;
    padding: 28px 32px;
    margin-bottom: 24px;
    border-radius: 22px;
    color: white;
    background:
        radial-gradient(circle at 85% 20%, rgba(96,165,250,.28), transparent 24%),
        linear-gradient(135deg, #0B1220, #172A4D 65%, #1D4ED8);
    box-shadow: 0 18px 45px rgba(11,18,32,.18);
    animation: fadeUp .65s ease both;
}

.hero::before {
    content: "";
    position: absolute;
    width: 230px;
    height: 230px;
    right: -70px;
    top: -110px;
    border-radius: 50%;
    background: rgba(34,211,238,.16);
    filter: blur(5px);
    animation: floatGlow 5s ease-in-out infinite;
}

.hero h1, .hero p {
    color: white !important;
    position: relative;
    z-index: 2;
}

.hero h1 {
    margin: 0;
    font-size: 2.1rem;
}

.hero p {
    margin: 8px 0 0;
    color: #CBD5E1 !important;
}

[data-testid="stMetric"] {
    background: rgba(255,255,255,.92);
    border: 1px solid var(--border);
    border-radius: 17px;
    padding: 17px 20px;
    box-shadow: 0 8px 24px rgba(15,23,42,.06);
    transition: transform .25s ease, box-shadow .25s ease, border-color .25s ease;
    animation: fadeUp .55s ease both;
}

[data-testid="stMetric"]:hover {
    transform: translateY(-5px);
    border-color: rgba(37,99,235,.35);
    box-shadow: 0 14px 32px rgba(37,99,235,.13);
}

[data-testid="stMetricLabel"] {
    color: var(--muted) !important;
}

[data-testid="stMetricValue"] {
    color: var(--navy) !important;
}

div[data-baseweb="input"],
div[data-baseweb="textarea"],
div[data-baseweb="select"] {
    border-radius: 11px;
}

div[data-baseweb="input"]:focus-within,
div[data-baseweb="textarea"]:focus-within,
div[data-baseweb="select"]:focus-within {
    box-shadow: 0 0 0 3px rgba(37,99,235,.12), 0 0 18px rgba(37,99,235,.08);
}

.stButton > button,
.stFormSubmitButton > button {
    border: 0 !important;
    border-radius: 11px !important;
    font-weight: 700 !important;
    padding: .62rem 1.15rem !important;
    background: linear-gradient(135deg, #2563EB, #1D4ED8) !important;
    color: white !important;
    box-shadow: 0 7px 18px rgba(37,99,235,.22) !important;
    transition: all .22s ease !important;
}

.stButton > button:hover,
.stFormSubmitButton > button:hover {
    transform: translateY(-2px) scale(1.015);
    box-shadow: 0 12px 26px rgba(37,99,235,.32) !important;
    filter: brightness(1.08);
}

.stButton > button:active,
.stFormSubmitButton > button:active {
    transform: translateY(1px) scale(.99);
}

[data-testid="stDataFrame"] {
    border-radius: 16px;
    overflow: hidden;
    border: 1px solid var(--border);
    box-shadow: 0 8px 24px rgba(15,23,42,.06);
}

div[data-testid="stAlert"] {
    border-radius: 13px;
    animation: fadeUp .35s ease both;
}

hr {
    border-color: var(--border) !important;
}

@keyframes fadeUp {
    from { opacity: 0; transform: translateY(14px); }
    to { opacity: 1; transform: translateY(0); }
}

@keyframes slideDown {
    from { opacity: 0; transform: translateY(-14px); }
    to { opacity: 1; transform: translateY(0); }
}

@keyframes floatGlow {
    0%, 100% { transform: translate(0,0) scale(1); }
    50% { transform: translate(-20px,20px) scale(1.08); }
}

@media (max-width: 768px) {
    .hero { padding: 22px; border-radius: 17px; }
    .hero h1 { font-size: 1.55rem; }
}
</style>
""", unsafe_allow_html=True)

# Iluminación interactiva con JavaScript.
components.html("""
<div id="light-layer"></div>
<script>
const layer = document.getElementById("light-layer");
layer.style.cssText = `
    position:fixed;
    inset:0;
    pointer-events:none;
    z-index:9999;
    background:radial-gradient(
        190px circle at 50% 50%,
        rgba(96,165,250,.12),
        transparent 72%
    );
    transition:background .08s linear;
`;
document.addEventListener("mousemove", (event) => {
    layer.style.background = `
        radial-gradient(
            190px circle at ${event.clientX}px ${event.clientY}px,
            rgba(96,165,250,.12),
            rgba(34,211,238,.035) 35%,
            transparent 72%
        )
    `;
});
</script>
""", height=0)

# =========================================================
# CLASE TICKET
# =========================================================

class TicketSoporte:

    PRIORIDADES = ["Baja", "Media", "Alta", "Crítica"]
    ESTADOS = ["Abierto", "En proceso", "Resuelto", "Cerrado"]

    def __init__(
        self,
        codigo,
        usuario,
        descripcion,
        prioridad,
        tecnico="Sin asignar"
    ):
        self.codigo = codigo
        self.usuario = usuario
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.estado = "Abierto"
        self.tecnico = tecnico
        self.fecha_creacion = datetime.now()


# =========================================================
# CLASE GESTOR DE TICKETS
# =========================================================

class GestorTickets:

    def __init__(self):
        self.tickets = {}


    # CREATE
    def crear_ticket(
        self,
        codigo,
        usuario,
        descripcion,
        prioridad,
        tecnico
    ):

        codigo = codigo.strip()
        usuario = usuario.strip()
        descripcion = descripcion.strip()
        tecnico = tecnico.strip()

        if codigo == "":
            return False, "El código no puede estar vacío."

        if codigo in self.tickets:
            return False, "Ya existe un ticket con ese código."

        if usuario == "":
            return False, "El usuario no puede estar vacío."

        if descripcion == "":
            return False, "La descripción no puede estar vacía."

        if prioridad not in TicketSoporte.PRIORIDADES:
            return False, "Prioridad no válida."

        if tecnico == "":
            tecnico = "Sin asignar"

        ticket = TicketSoporte(
            codigo,
            usuario,
            descripcion,
            prioridad,
            tecnico
        )

        self.tickets[codigo] = ticket

        return True, "Ticket creado correctamente."


    # READ
    def buscar_ticket(self, codigo):

        return self.tickets.get(codigo)


    def listar_tickets(self):

        return list(self.tickets.values())


    # UPDATE
    def actualizar_ticket(
        self,
        codigo,
        usuario,
        descripcion,
        prioridad,
        estado,
        tecnico
    ):

        ticket = self.tickets.get(codigo)

        if not ticket:
            return False, "Ticket no encontrado."

        if usuario.strip() == "":
            return False, "El usuario no puede estar vacío."

        if descripcion.strip() == "":
            return False, "La descripción no puede estar vacía."

        if prioridad not in TicketSoporte.PRIORIDADES:
            return False, "Prioridad no válida."

        if estado not in TicketSoporte.ESTADOS:
            return False, "Estado no válido."

        ticket.usuario = usuario
        ticket.descripcion = descripcion
        ticket.prioridad = prioridad
        ticket.estado = estado
        ticket.tecnico = tecnico if tecnico.strip() else "Sin asignar"

        return True, "Ticket actualizado correctamente."


    # DELETE
    def eliminar_ticket(self, codigo):

        if codigo in self.tickets:

            del self.tickets[codigo]

            return True, "Ticket eliminado correctamente."

        return False, "Ticket no encontrado."


# =========================================================
# SESSION STATE
# =========================================================

if "gestor" not in st.session_state:

    st.session_state.gestor = GestorTickets()


gestor = st.session_state.gestor


# =========================================================
# ENCABEZADO
# =========================================================

st.markdown("""
<div class="hero">
    <h1>🛠️ Sistema de Soporte Técnico</h1>
    <p>Gestión empresarial de incidencias mediante operaciones CRUD.</p>
</div>
""", unsafe_allow_html=True)


# =========================================================
# MENÚ LATERAL
# =========================================================

st.sidebar.markdown("## 🏢 Mesa de Ayuda")
st.sidebar.caption("Centro de gestión de incidencias")

opcion = st.sidebar.radio(
    "Módulos",
    [
        "Inicio",
        "Crear ticket",
        "Consultar tickets",
        "Actualizar ticket",
        "Eliminar ticket"
    ]
)


# =========================================================
# INICIO
# =========================================================

if opcion == "Inicio":

    st.subheader("Panel principal")

    tickets = gestor.listar_tickets()

    total = len(tickets)

    abiertos = len([
        t for t in tickets
        if t.estado == "Abierto"
    ])

    proceso = len([
        t for t in tickets
        if t.estado == "En proceso"
    ])

    resueltos = len([
        t for t in tickets
        if t.estado == "Resuelto"
    ])

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total tickets", total)

    col2.metric("Abiertos", abiertos)

    col3.metric("En proceso", proceso)

    col4.metric("Resueltos", resueltos)


    st.subheader("Tickets recientes")

    if tickets:

        datos = []

        for ticket in tickets:

            datos.append({
                "Código": ticket.codigo,
                "Usuario": ticket.usuario,
                "Prioridad": ticket.prioridad,
                "Estado": ticket.estado,
                "Técnico": ticket.tecnico,
                "Fecha": ticket.fecha_creacion.strftime(
                    "%d/%m/%Y %H:%M"
                )
            })

        st.dataframe(
            datos,
            use_container_width=True
        )

    else:

        st.info(
            "Todavía no existen tickets registrados."
        )


# =========================================================
# CREATE
# =========================================================

elif opcion == "Crear ticket":

    st.subheader("➕ Crear nuevo ticket")

    with st.form("form_crear_ticket"):

        codigo = st.text_input(
            "Código del ticket",
            placeholder="Ejemplo: TK001"
        )

        usuario = st.text_input(
            "Usuario solicitante",
            placeholder="Ejemplo: Carlos Carrillo"
        )

        descripcion = st.text_area(
            "Descripción del problema",
            placeholder="Describa el problema técnico..."
        )

        prioridad = st.selectbox(
            "Prioridad",
            TicketSoporte.PRIORIDADES
        )

        tecnico = st.text_input(
            "Técnico asignado",
            placeholder="Opcional"
        )

        guardar = st.form_submit_button(
            "Registrar ticket"
        )


    if guardar:

        resultado, mensaje = gestor.crear_ticket(
            codigo,
            usuario,
            descripcion,
            prioridad,
            tecnico
        )

        if resultado:

            st.success(mensaje)

        else:

            st.error(mensaje)


# =========================================================
# READ
# =========================================================

elif opcion == "Consultar tickets":

    st.subheader("🔎 Consultar tickets")


    tipo_consulta = st.radio(
        "Seleccione una opción",
        [
            "Mostrar todos",
            "Buscar por código"
        ],
        horizontal=True
    )


    # -----------------------
    # MOSTRAR TODOS
    # -----------------------

    if tipo_consulta == "Mostrar todos":

        tickets = gestor.listar_tickets()

        if tickets:

            datos = []

            for ticket in tickets:

                datos.append({

                    "Código": ticket.codigo,

                    "Usuario": ticket.usuario,

                    "Descripción": ticket.descripcion,

                    "Prioridad": ticket.prioridad,

                    "Estado": ticket.estado,

                    "Técnico": ticket.tecnico,

                    "Fecha": ticket.fecha_creacion.strftime(
                        "%d/%m/%Y %H:%M"
                    )

                })

            st.dataframe(
                datos,
                use_container_width=True,
                hide_index=True
            )

        else:

            st.info(
                "No existen tickets registrados."
            )


    # -----------------------
    # BUSCAR POR CÓDIGO
    # -----------------------

    else:

        codigo_busqueda = st.text_input(
            "Ingrese el código del ticket"
        )

        if st.button("Buscar"):

            ticket = gestor.buscar_ticket(
                codigo_busqueda
            )

            if ticket:

                st.success(
                    "Ticket encontrado"
                )

                col1, col2 = st.columns(2)

                with col1:

                    st.write(
                        "**Código:**",
                        ticket.codigo
                    )

                    st.write(
                        "**Usuario:**",
                        ticket.usuario
                    )

                    st.write(
                        "**Prioridad:**",
                        ticket.prioridad
                    )


                with col2:

                    st.write(
                        "**Estado:**",
                        ticket.estado
                    )

                    st.write(
                        "**Técnico:**",
                        ticket.tecnico
                    )

                    st.write(
                        "**Fecha:**",
                        ticket.fecha_creacion.strftime(
                            "%d/%m/%Y %H:%M"
                        )
                    )


                st.write(
                    "**Descripción del problema:**"
                )

                st.info(
                    ticket.descripcion
                )

            else:

                st.error(
                    "Ticket no encontrado."
                )


# =========================================================
# UPDATE
# =========================================================

elif opcion == "Actualizar ticket":

    st.subheader("✏️ Actualizar ticket")

    if len(gestor.tickets) == 0:

        st.info(
            "No existen tickets para actualizar."
        )

    else:

        codigos = list(
            gestor.tickets.keys()
        )

        codigo = st.selectbox(
            "Seleccione un ticket",
            codigos
        )

        ticket = gestor.buscar_ticket(
            codigo
        )


        with st.form("form_actualizar"):

            usuario = st.text_input(
                "Usuario",
                value=ticket.usuario
            )

            descripcion = st.text_area(
                "Descripción",
                value=ticket.descripcion
            )


            prioridad = st.selectbox(
                "Prioridad",
                TicketSoporte.PRIORIDADES,
                index=TicketSoporte.PRIORIDADES.index(
                    ticket.prioridad
                )
            )


            estado = st.selectbox(
                "Estado",
                TicketSoporte.ESTADOS,
                index=TicketSoporte.ESTADOS.index(
                    ticket.estado
                )
            )


            tecnico = st.text_input(
                "Técnico asignado",
                value=ticket.tecnico
            )


            actualizar = st.form_submit_button(
                "Actualizar ticket"
            )


        if actualizar:

            resultado, mensaje = gestor.actualizar_ticket(
                codigo,
                usuario,
                descripcion,
                prioridad,
                estado,
                tecnico
            )

            if resultado:

                st.success(mensaje)

            else:

                st.error(mensaje)


# =========================================================
# DELETE
# =========================================================

elif opcion == "Eliminar ticket":

    st.subheader("🗑️ Eliminar ticket")


    if len(gestor.tickets) == 0:

        st.info(
            "No existen tickets para eliminar."
        )


    else:

        codigo = st.selectbox(
            "Seleccione el ticket",
            list(gestor.tickets.keys())
        )


        ticket = gestor.buscar_ticket(
            codigo
        )


        st.warning(
            f"""
            Está a punto de eliminar el ticket **{ticket.codigo}**
            correspondiente al usuario **{ticket.usuario}**.
            """
        )


        confirmar = st.checkbox(
            "Confirmo que deseo eliminar este ticket"
        )


        if st.button(
            "Eliminar ticket",
            type="primary"
        ):

            if confirmar:

                resultado, mensaje = gestor.eliminar_ticket(
                    codigo
                )

                if resultado:

                    st.success(mensaje)

                    st.rerun()

                else:

                    st.error(mensaje)

            else:

                st.warning(
                    "Debe confirmar la eliminación."
                )
