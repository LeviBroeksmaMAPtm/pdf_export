from fpdf import FPDF;
import time;

timestamp = time.time();
time_alert = "26-07-2021 14:52";
origin_alert = "sWIS";
type_of_incident = "Overig";
creator = "Levi";
width = 210;
height= 297;

# definieer portret modus, afmetingen in mm en pagina formaat A4
pdf = FPDF('P', 'mm', 'A4')
#creëer de pagina
pdf.add_page()
# definieer de titel
pdf.set_font('Arial', 'B', 16)
pdf.cell(ln=1, h=15, align='L', w=0, txt="Rapportage incident: 'incidentnummer hier' 'datum incident hier'")
# definieer de gegevens van de melding
pdf.set_font('Arial', '', 14)
pdf.cell(ln=1, h=7, w=20,txt=f'Aangemaakt door: {creator}')
pdf.cell(ln=1, h=7, w=20,txt=f'Tijdstip melding: {time_alert}')
pdf.cell(ln=1, h=7, w=20,txt=f'Type incident: {type_of_incident}')
pdf.cell(ln=1, h=7, w=20,txt=f'Herkomst melding: {origin_alert}')
pdf.cell(ln=1, h=7, w=20,txt=f'------------------------------------------------------------------------------------------------------------------')
# genereer de afbeelding
pdf.image("./resources/pexels-pixabay-48125.jpeg", 12, 65, width - 24)


pdf.output(f'{timestamp}.pdf', 'F')