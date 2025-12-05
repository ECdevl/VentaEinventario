
# 🏪 Sistema de Ventas e Inventario (POS & Inventory Management System)

A complete point-of-sale (POS) and inventory management system built with Python Tkinter. Designed for small businesses to manage their sales, track inventory, and maintain product records efficiently.

## ✨ Features

### Sales Management
- **Product Selection**: Choose products from inventory with dropdown menu
- **Quantity Control**: Adjust quantities for each sale
- **Real-time Total**: Automatic calculation of sale totals in ARS (Argentine Pesos)
- **Multiple Payment Methods**: Support for cash, card, and bank transfers
- **Sales History**: View and track all completed transactions

### Inventory Management
- **Product Database**: Add, edit, and delete products
- **Stock Tracking**: Monitor product quantities and costs
- **Unique Product Codes**: Each product identified by unique code
- **Product Information**: Store product name, quantity, cost, and code
- **Inventory Overview**: Complete list of all products with details

### Business Operations
- **Cash Register**: Dedicated interface for daily cash operations
- **Dual Module System**: Separate sales and inventory modules
- **Data Persistence**: All data saved locally using SQL database

## 🖼️ Screenshots

<img width="798" height="398" alt="Screenshot_1" src="https://github.com/user-attachments/assets/6e839dd3-23e7-4b28-85f2-eb200f5c8f2c" />
<img width="1002" height="502" alt="Screenshot_3" src="https://github.com/user-attachments/assets/c2c72c95-c502-4b80-b426-855b1a361edb" />
<img width="997" height="501" alt="Screenshot_2" src="https://github.com/user-attachments/assets/6e582b00-9faf-4a0e-ab46-aa7dc8eac3ee" />

## 🛠️ Built With

- **Python** - Core programming language
- **Tkinter** - GUI framework for desktop interface
- **SQLite** - Local database for data persistence
- **SQL** - Database queries and management

## 📥 Installation

### Windows
1. Download the latest release from [Releases](https://github.com/ECdevl/pos-inventory-system/releases)
2. Extract the ZIP file
3. Run `POS_System.exe`

### Linux
1. Download the Linux build from [Releases](https://github.com/ECdevl/pos-inventory-system/releases)
2. Make it executable: `chmod +x POS_System`
3. Run: `./POS_System`

## 🚀 Usage

### Starting the System
1. Launch the application
2. Choose between three modules:
   - **Ventas** (Sales): Process customer transactions
   - **Inventario** (Inventory): Manage products and stock
   - **Hacer Caja** (Cash Register): Handle cash operations

### Managing Inventory
1. Click "Inventario" from the main menu
2. Fill in product details:
   - Product name
   - Quantity in stock
   - Cost per unit
   - Unique product code
3. Click "Agregar" to add new products
4. Use "Editar" to modify existing products
5. Click "Eliminar" to remove products

### Processing Sales
1. Click "Ventas" from the main menu
2. Select product from dropdown menu
3. Enter quantity to sell
4. Click "Agregar" to add to cart
5. Review items in "Artículos a vender" list
6. Select payment method (Transferencia, Efectivo, Tarjeta)
7. Click "Finalizar Compra" to complete the sale
8. Total is displayed in ARS currency

## 💻 Running from Source

```bash
# Clone the repository
git clone https://github.com/ECdevl/pos-inventory-system.git

# Navigate to project directory
cd pos-inventory-system

# No additional dependencies needed (Tkinter included with Python)
# SQLite is built into Python

# Run the application
python main.py
```

## 🔧 Technical Highlights

- **SQL Database Integration**: Local SQLite database for reliable data storage
- **CRUD Operations**: Complete Create, Read, Update, Delete functionality
- **Real-time Calculations**: Automatic price and total calculations
- **Modular Architecture**: Separate modules for sales, inventory, and cash management
- **Desktop-Optimized**: Built specifically for desktop environments with Tkinter

## 📊 Database Structure

The system uses SQLite with tables for:
- **Products**: Store inventory items with details
- **Sales**: Record all transactions
- **Sales Items**: Individual items per sale for detailed tracking

## 📝 Future Improvements

- [ ] Sales reports and analytics
- [ ] Low stock alerts
- [ ] Barcode scanner integration
- [ ] Receipt printing functionality
- [ ] Multi-user support with authentication
- [ ] Product categories and filters
- [ ] Sales history export (PDF, Excel)
- [ ] Customer database integration
- [ ] Profit margin calculations
- [ ] Monthly/yearly sales statistics

## 👤 Author

**ECdevl**
- GitHub: [@ECdevl](https://github.com/ECdevl)
- LinkedIn: [Your LinkedIn Profile]

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

⭐ If you found this project useful, please consider giving it a star!

## 💼 Use Cases

Perfect for:
- Small retail stores
- Neighborhood shops
- Small business inventory management
- Learning SQL and database integration
- Desktop application development with Python
