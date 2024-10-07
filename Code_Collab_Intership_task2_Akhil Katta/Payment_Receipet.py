from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime


def generate_receipt(customer_name, amount, date, transaction_id):
    
    file_name = f"receipt_{transaction_id}.pdf"
    pdf = canvas.Canvas(file_name, pagesize=A4)
    
    
    pdf.setTitle(f"Receipt_{transaction_id}")
    
    
    pdf.setFont("Helvetica", 16)
    pdf.drawString(200, 800, "Payment Receipt")
    
    
    pdf.setFont("Helvetica", 12)
    pdf.drawString(50, 750, f"Customer Name: {customer_name}")
    pdf.drawString(50, 725, f"Amount Paid: ${amount}")
    pdf.drawString(50, 700, f"Date: {date}")
    pdf.drawString(50, 675, f"Transaction ID: {transaction_id}")
    
    
    pdf.showPage()
    pdf.save()
    
    print(f"Receipt generated successfully: {file_name}")


def get_payment_details():
    customer_name = input("Enter customer name: ")
    amount = input("Enter amount: ")
    transaction_id = input("Enter transaction ID: ")
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    return customer_name, amount, date, transaction_id


def main():
    print("Welcome to the Payment Receipt Generator!")
    customer_name, amount, date, transaction_id = get_payment_details()
    generate_receipt(customer_name, amount, date, transaction_id)

if __name__ == "__main__":
    main()
