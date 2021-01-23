from PyQt5.QtWidgets import (QApplication, QWidget, QFrame, QVBoxLayout, QHBoxLayout, QGridLayout,
                             QGroupBox, QLabel, QCheckBox, QPushButton, QLineEdit, QMessageBox)
from PyQt5.QtGui import QFont, QIcon, QPixmap, QColor
from PyQt5.QtCore import Qt, QSize, QDate, QTime, QDateTime

import sys

class RestaurantBillingSystem(QWidget):
    invoice_no = 0
    def __init__(self, parent=None, **options):
        super(RestaurantBillingSystem, self).__init__(parent, **options)
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle("Restaurant Billing System")
        self.setWindowIcon(QIcon("sandwitch2.jpg"))
        self.setLayoutDirection(Qt.RightToLeft)
        self.setGeometry(50, 50, 1500, 900)
        self.setFixedSize(1500, 900)
        bgColor = QColor(150, 150, 150)
        fgColor = QColor(0, 0, 0)
        mainStyle = "background-color: {}; color: {}".format(bgColor.name(), fgColor.name())
        mainFont = QFont("urdu Typesetting", 14, 900)
        self.setStyleSheet(mainStyle)
        self.setFont(mainFont)

        self.createTitle()
        self.createMeals()
        self.createDrinks()
        self.createReciept()


        vBox = QVBoxLayout()
        #title
        vBox.addLayout(self.titlContainer)
        hBox = QHBoxLayout()
        #body
        hBox.addWidget(self.mealContainer)
        hBox.addWidget(self.drinkContainer)
        hBox.addWidget(self.recieptContainer)

        vBox.addLayout(hBox)
        vBox.addStretch()
        self.setLayout(vBox)

    #***************************************************create main title ****************************
    def createTitle(self):
        self.titlContainer = QHBoxLayout()
        self.lblTitle = QLabel("مطعم الوجبات السريعة - إدارة المبيعات", self)
        fontTitle = QFont("urdu Typesetting", 48, 900)
        fontTitle.setBold(True)
        bgTitle = QColor(100, 100, 100)
        fgTitle = QColor(200, 150, 40)
        bdTitle = QColor(70, 70, 70)
        lbdTitle = QColor(0, 0, 0)
        sizeTitle = QSize(1480, 160)

        styleTitle = "background-color: {}; color: {}; border: 10px solid {}; border-left: 15px solid {}; border-right: 10 solid {}".format(
            bgTitle.name(), fgTitle.name(), bdTitle.name(), lbdTitle.name(), lbdTitle.name()
        )
        self.lblTitle.setFont(fontTitle)
        self.lblTitle.setStyleSheet(styleTitle)
        self.lblTitle.setFixedSize(sizeTitle)
        self.lblTitle.setAlignment(Qt.AlignCenter)
        self.titlContainer.addWidget(self.lblTitle)

    # ***************************************************create meals list ****************************
    def createMeals(self):
        self.mealContainer = QFrame(self)
        self.mealContainer.setFixedSize(500, 700)
        vbox = QVBoxLayout()
        self.mealGroup = QGroupBox("اختار وجبتك", self)
        self.mealGroup.setFont(QFont("urdu Typesetting", 36, 900))
        mealGrid = QGridLayout()
        self.lblMeal = QLabel("الوجبة", self)
        self.lblPrice = QLabel("السعر(ج.م)", self)
        self.lblQuantity = QLabel("الكمية", self)
        mealHeaders = [self.lblMeal, self.lblPrice, self.lblQuantity]
        for h, head in enumerate(mealHeaders):
            head.setFont(QFont("urdu Typesetting", 18, 900))
            head.setFixedSize(80, 40)
            head.setAlignment(Qt.AlignCenter)
            head.setStyleSheet("background-color: grey; color: black; border: 1px solid black; border-radius:10px")
            mealGrid.addWidget(head, 0, h, 1, 1)

        self.chkShrimp = QCheckBox("الجمبري مع أرز", self)
        self.chkShrimp.toggled.connect(lambda : self.selectedItem(self.chkShrimp, self.shrimpPrice, self.QShrimp))
        self.chkFish = QCheckBox("السمك مع أرز", self)
        self.chkFish.toggled.connect(lambda : self.selectedItem(self.chkFish, self.fishPrice, self.QFish))
        self.chkBeef = QCheckBox("طاجن اللحم مع أرز", self)
        self.chkBeef.toggled.connect(lambda: self.selectedItem(self.chkBeef, self.beefPrice, self.QBeef))
        self.chkChicken = QCheckBox("الفراخ مع أرز", self)
        self.chkChicken.toggled.connect(lambda: self.selectedItem(self.chkChicken, self.chickenPrice, self.QChicken))
        self.chkBeefShawarma = QCheckBox("شاروما لحم مع الأرز", self)
        self.chkBeefShawarma.toggled.connect(lambda: self.selectedItem(self.chkBeefShawarma, self.beefShawarmaPrice, self.QBeefShawarma))
        self.chkChickenShawarma= QCheckBox("شاورما فراخ مع الأرز", self)
        self.chkChickenShawarma.toggled.connect(lambda: self.selectedItem(self.chkChickenShawarma, self.chickenShawarmaPrice, self.QChickenShawarma))
        self.chkMeatRiceNuts = QCheckBox("لحم مع أرز بالمكسرات", self)
        self.chkMeatRiceNuts.toggled.connect(lambda: self.selectedItem(self.chkMeatRiceNuts, self.meatRicePrice, self.QMeatRiceNuts))
        self.chkMeatKofta = QCheckBox("كفتة لحم مع الأرز", self)
        self.chkMeatKofta.toggled.connect(lambda: self.selectedItem(self.chkMeatKofta, self.meatKoftaPrice, self.QMeatKofta))
        self.chkVegetables = QCheckBox("خضراوات مع الأرز", self)
        self.chkVegetables.toggled.connect(lambda: self.selectedItem(self.chkVegetables, self.vegetablesPrice, self.QVegetables))
        chkMeals = [
            self.chkShrimp, self.chkFish, self.chkBeef, self.chkChicken,
            self.chkBeefShawarma, self.chkChickenShawarma, self.chkMeatRiceNuts,
            self.chkMeatKofta, self.chkVegetables
        ]
        chkFont = QFont("Traditinal Arabic", 20, 900)
        # chkFont.setBold(True)
        # chkColor = QColor(30, 30, 200)
        chkStyle = "padding: 3px"
        for m, meal in enumerate(chkMeals):
            meal.setFont(chkFont)
            meal.setStyleSheet(chkStyle)
            mealGrid.addWidget(meal, m+1, 0, 1, 1)

        self.shrimpPrice = QLabel("45.00", self)
        self.fishPrice = QLabel("45.00", self)
        self.beefPrice = QLabel("45.00", self)
        self.chickenPrice = QLabel("40.50", self)
        self.beefShawarmaPrice = QLabel("40.50", self)
        self.chickenShawarmaPrice = QLabel("40.50", self)
        self.meatRicePrice = QLabel("45.50", self)
        self.meatKoftaPrice = QLabel("45.50", self)
        self.vegetablesPrice = QLabel("35.50", self)

        lblPrices = [
            self.shrimpPrice, self.fishPrice, self.beefPrice, self.chickenPrice,
            self.beefShawarmaPrice, self.chickenShawarmaPrice, self.meatRicePrice,
            self.meatKoftaPrice, self.vegetablesPrice
        ]

        for p, price in enumerate(lblPrices):
            price.setFont(chkFont)
            price.setAlignment(Qt.AlignCenter)
            mealGrid.addWidget(price, p+1, 1, 1, 1)

        self.QShrimp = QLineEdit("0", self)
        self.QFish = QLineEdit("0", self)
        self.QBeef = QLineEdit("0", self)
        self.QChicken = QLineEdit("0", self)
        self.QBeefShawarma = QLineEdit("0", self)
        self.QChickenShawarma = QLineEdit("0", self)
        self.QMeatRiceNuts = QLineEdit("0", self)
        self.QMeatKofta = QLineEdit("0", self)
        self.QVegetables = QLineEdit("0", self)
        quantities = [
            self.QShrimp, self.QFish, self.QBeef, self.QChicken,
            self.QBeefShawarma, self.QChickenShawarma, self.QMeatRiceNuts,
            self.QMeatKofta, self.QVegetables
        ]
        for q, quantity in enumerate(quantities):
            quantity.setFixedSize(80, 40)
            quantity.setAlignment(Qt.AlignCenter)
            quantity.setFont(QFont("urdu Typesetting", 20))
            mealGrid.addWidget(quantity, q+1, 2, 1, 1)


        self.mealGroup.setLayout(mealGrid)

        vbox.addWidget(self.mealGroup)

        self.ctrlGroup = QGroupBox("إصدار فاتورة", self)
        self.ctrlGroup.setFont(QFont("urdu Typesetting", 14))
        ctrlFont = QFont("urdu Typesetting", 18, 900)
        ctrlSize = QSize(110, 60)
        ctrlbgColor = QColor(20, 70, 150)
        ctrlfgColor = QColor(200, 200, 200)
        ctrlStyle = "background-color: {}; color: {}; border: 3px solid {}; border-radius: 10px".format(
            ctrlbgColor.name(), ctrlfgColor.name(), ctrlfgColor.name())
        ctrlGrid = QGridLayout()
        self.getTotals = QPushButton("حساب الإجمالي", self)
        self.getTotals.clicked.connect(self.getTotalAction)
        self.getInvoice = QPushButton("طباعة الفاتورة", self)
        self.getInvoice.clicked.connect(self.getInvoiceAction)
        self.clearData = QPushButton("فاتورة جديدة", self)
        self.clearData.clicked.connect(self.newTransaction)
        self.exitProgram = QPushButton("خروج", self)
        self.exitProgram.clicked.connect(self.exit_pro)
        controls = [self.getTotals, self.getInvoice, self.clearData, self.exitProgram]
        for c, ctrl in enumerate(controls):
            ctrl.setFont(ctrlFont)
            ctrl.setFixedSize(ctrlSize)
            ctrl.setStyleSheet(ctrlStyle)
            ctrlGrid.addWidget(ctrl, 0, c, 1, 1)

        self.ctrlGroup.setLayout(ctrlGrid)
        vbox.addWidget(self.ctrlGroup)
        self.mealContainer.setLayout(vbox)

    # ***************************************************create drinks menu ****************************
    def createDrinks(self):
        self.drinkContainer = QFrame(self)
        self.drinkContainer.setFixedSize(500, 700)

        vbox = QVBoxLayout()
        self.drinkGroup = QGroupBox("اختار مشروبك", self)
        self.drinkGroup.setFont(QFont("urdu Typesetting", 36, 900))
        drinkGrid = QGridLayout()
        self.lblDrink = QLabel("المشروب", self)
        self.lblDrinkPrice = QLabel("السعر(ج.م)", self)
        self.lblDrinkQuantity = QLabel("الكمية", self)
        drinkHeaders = [self.lblDrink, self.lblDrinkPrice, self.lblDrinkQuantity]
        for h, head in enumerate(drinkHeaders):
            head.setFont(QFont("urdu Typesetting", 18, 900))
            head.setFixedSize(80, 40)
            head.setAlignment(Qt.AlignCenter)
            head.setStyleSheet("background-color: grey; color: black; border: 1px solid black; border-radius:10px")
            drinkGrid.addWidget(head, 0, h, 1, 1)

        self.chkCappuccino = QCheckBox("كابوتشـــــــــــينو", self)
        self.chkCappuccino.toggled.connect(
            lambda: self.selectedItem(self.chkCappuccino, self.priceCappuccino, self.QCappuccino))
        self.chkEspresso = QCheckBox("إسبريســـــــــو", self)
        self.chkEspresso.toggled.connect(
            lambda: self.selectedItem(self.chkEspresso, self.priceEspresso, self.QEspresso))
        self.chkTurkishCoffee = QCheckBox("قهـــــــوة تركـــي", self)
        self.chkTurkishCoffee.toggled.connect(
            lambda: self.selectedItem(self.chkTurkishCoffee, self.priceTurkishCoffee, self.QTurkishCoffee))
        self.chkBackTea = QCheckBox("شــــــــــاي أحمــر", self)
        self.chkBackTea.toggled.connect(
            lambda: self.selectedItem(self.chkBackTea, self.priceBlackTea, self.QBlackTea))
        self.chkGreenTea = QCheckBox("شـــــــــاي أخضـــر", self)
        self.chkGreenTea.toggled.connect(
            lambda: self.selectedItem(self.chkGreenTea, self.priceGreenTea, self.QGreenTea))
        self.chkOrangeJuice = QCheckBox("عصيــــــــر برتقـــال", self)
        self.chkOrangeJuice.toggled.connect(
            lambda: self.selectedItem(self.chkOrangeJuice, self.priceOrangeJuice, self.QOrangeJuice))
        self.chkLemonade = QCheckBox("عصيــــــــر ليمـــون", self)
        self.chkLemonade.toggled.connect(
            lambda: self.selectedItem(self.chkLemonade, self.priceLemonade, self.QLemonade))
        self.chGreenApple = QCheckBox("تفــــــــــاح أخضــــر", self)
        self.chGreenApple.toggled.connect(
            lambda: self.selectedItem(self.chGreenApple, self.priceGreenApple, self.QGreenApple))
        self.chkWaterBottle = QCheckBox("زجاجـــــــــة ميـــــاه", self)
        self.chkWaterBottle.toggled.connect(
            lambda: self.selectedItem(self.chkWaterBottle, self.priceWater, self.QWaterBottle))
        chkDrinks = [
            self.chkCappuccino, self.chkEspresso, self.chkTurkishCoffee, self.chkBackTea,
            self.chkGreenTea, self.chkOrangeJuice, self.chkLemonade,
            self.chGreenApple, self.chkWaterBottle
        ]
        chkFont = QFont("Traditional Arabic", 20)
        chkFont.setBold(True)
        # chkColor = QColor(30, 30, 200)
        chkStyle = "padding: 3px"
        for d, drink in enumerate(chkDrinks):
            drink.setFont(chkFont)
            drink.setStyleSheet(chkStyle)
            drinkGrid.addWidget(drink, d + 1, 0, 1, 1)


        self.priceCappuccino = QLabel("27.00", self)
        self.priceEspresso = QLabel("22.00", self)
        self.priceTurkishCoffee = QLabel("15.00", self)
        self.priceBlackTea = QLabel("10.00", self)
        self.priceGreenTea = QLabel("12.00", self)
        self.priceOrangeJuice = QLabel("18.00", self)
        self.priceLemonade = QLabel("18.00", self)
        self.priceGreenApple = QLabel("18.00", self)
        self.priceWater = QLabel("5.00", self)

        lblPrices = [
            self.priceCappuccino, self.priceEspresso, self.priceTurkishCoffee, self.priceBlackTea,
            self.priceGreenTea, self.priceOrangeJuice, self.priceLemonade,
            self.priceGreenApple, self.priceWater
        ]

        for p, price in enumerate(lblPrices):
            price.setFont(chkFont)
            price.setAlignment(Qt.AlignCenter)
            drinkGrid.addWidget(price, p + 1, 1, 1, 1)


        self.QCappuccino = QLineEdit("0", self)
        self.QEspresso = QLineEdit("0", self)
        self.QTurkishCoffee = QLineEdit("0", self)
        self.QBlackTea = QLineEdit("0", self)
        self.QGreenTea= QLineEdit("0", self)
        self.QOrangeJuice = QLineEdit("0", self)
        self.QLemonade = QLineEdit("0", self)
        self.QGreenApple = QLineEdit("0", self)
        self.QWaterBottle = QLineEdit("0", self)
        quantities = [
            self.QCappuccino, self.QEspresso, self.QTurkishCoffee, self.QBlackTea,
            self.QGreenTea, self.QOrangeJuice, self.QLemonade,
            self.QGreenApple, self.QWaterBottle
        ]
        for q, quantity in enumerate(quantities):
            quantity.setFixedSize(80, 40)
            quantity.setAlignment(Qt.AlignCenter)
            quantity.setFont(QFont("urdu Typesetting", 20))
            drinkGrid.addWidget(quantity, q + 1, 2, 1, 1)

        self.drinkGroup.setLayout(drinkGrid)
        vbox.addWidget(self.drinkGroup)
        self.resultGroup=QGroupBox("حساب الإجمالي",self)
        self.resultGroup.setFont(QFont("urdu Typesetting", 14, 900))
        resultGrid = QGridLayout()
        self.lblTotal = QLabel("الإجمالي", self)
        self.scrTotal = QLabel("0", self)
        self.lblDiscount = QLabel("خصم نقدي", self)
        self.scrDiscount = QLabel("0", self)
        self.lblVAT = QLabel("ضريبة ق.م", self)
        self.scrVAT = QLabel("0", self)
        self.lblNetValue = QLabel("الصافي", self)
        self.scrNetValue = QLabel("0", self)

        results = [
            [self.lblTotal, self.scrTotal, self.lblDiscount, self.scrDiscount],
            [self.lblVAT, self.scrVAT, self.lblNetValue, self.scrNetValue]
        ]
        for r, row in enumerate(results):
            for c, col in enumerate(row):
                col.setFont(QFont("urdu Typesetting", 14))
                col.setFixedSize(80, 40)
                resultGrid.addWidget(col, r, c, 1, 1)

        self.resultGroup.setLayout(resultGrid)
        vbox.addWidget(self.resultGroup)

        self.drinkContainer.setLayout(vbox)

    # ***************************************************create invoice details ****************************
    def createReciept(self):
        self.recieptContainer = QFrame(self)
        self.recieptContainer.setFixedSize(500, 700)
        vbox = QVBoxLayout()
        self.recieptGroup = QGroupBox("تفاصيل الفاتورة", self)
        self.recieptGroup.setFont(QFont("urdu Typesetting", 36, 900))
        recieptGrid = QGridLayout()
        date = QDate.currentDate()
        time = QTime.currentTime()
        invNumber = QDateTime.currentDateTime()

        headerFont = QFont("Traditional Arabic", 10, 900)
        headerFont.setBold(True)
        self.recHeader = QLabel("مطعم الوجبات السريعة", self)
        self.recHeader.setFont(QFont("Traditional Arabic", 18, 900))
        self.recHeader.setAlignment(Qt.AlignCenter)
        recieptGrid.addWidget(self.recHeader, 0, 0, 1, 4)
        self.recTime = QLabel(self)
        self.recTime.setText( "الوقت:"+time.toString(Qt.DefaultLocaleLongDate))
        self.recDate = QLabel(self)
        self.recDate.setText("التاريخ: " + date.toString(Qt.ISODate))
        self.recNumbertext = QLabel("رقم الفاتورة : ", self)
        self.recNumberValue = QLabel(self)
        self.recNumberValue.setStyleSheet("padding-left: 2px")
        self.recNumberValue.setText(invNumber.toString(Qt.ISODate)+" "+str(RestaurantBillingSystem.invoice_no))
        titles = [self.recNumbertext, self.recNumberValue, self.recTime, self.recDate]
        for t, title in enumerate(titles):
            title.setFont(QFont("Traditional Arabic", 12, 900))
            title.setAlignment(Qt.AlignCenter)
            recieptGrid.addWidget(title, 1, t, 1, 1)

        self.itemName = QLabel("الصنف", self)
        self.itemPrice = QLabel("السعر(ج.م)", self)
        self.itemQuantity = QLabel("الكمية", self)
        self.itemTotal = QLabel("الإجمالي", self)
        headers = [self.itemName, self.itemPrice, self.itemQuantity, self.itemTotal]
        for h, head in enumerate(headers):
            head.setFont(headerFont)
            head.setAlignment(Qt.AlignCenter)
            head.setFixedSize(120, 30)
            recieptGrid.addWidget(head, 2, h, 1, 1)

        self.scrReciept = QLabel(self)
        self.scrReciept.setFixedSize(460, 330)
        scrFont = QFont("Arabic Transparent", 12, 900)
        scrFont.setBold(True)
        self.scrReciept.setFont(scrFont)
        self.scrReciept.setStyleSheet("padding-left: 5px")
        recieptGrid.addWidget(self.scrReciept, 3, 0, 1, 4)

        self.invTotal = QLabel("الإجمالي", self)
        recieptGrid.addWidget(self.invTotal, 4, 0, 1, 3)
        self.totalValue = QLabel(self)
        recieptGrid.addWidget(self.totalValue, 4, 3, 1, 1)

        self.invDiscount = QLabel("خصم نقدي", self)
        recieptGrid.addWidget(self.invDiscount, 5, 0, 1, 3)
        self.disValue = QLabel(self)
        recieptGrid.addWidget(self.disValue, 5, 3, 1, 1)

        self.invVAT = QLabel("ضريبة ق.م", self)
        recieptGrid.addWidget(self.invVAT, 6, 0, 1, 3)
        self.VATValue = QLabel(self)
        recieptGrid.addWidget(self.VATValue, 6, 3, 1, 1)

        self.invNetText = QLabel("صافي الفاتورة", self)
        recieptGrid.addWidget(self.invNetText, 7, 0, 1, 3)
        self.netValue = QLabel(self)
        recieptGrid.addWidget(self.netValue, 7, 3, 1, 1)

        self.totals = [self.invTotal, self.totalValue, self.invDiscount, self.disValue,
                       self.invVAT, self.VATValue, self.invNetText, self.netValue
                       ]
        for tot in self.totals:
            tot.setFont(QFont("Traditional Arabic", 12, 900))
            tot.setAlignment(Qt.AlignLeft)
            tot.setStyleSheet("padding-left: 30")
            tot.setMinimumHeight(30)
        self.totValues = [self.totalValue, self.disValue, self.VATValue, self.netValue]
        valfont = QFont("Traditional Arabic", 14, 900)
        valfont.setBold(True)
        for val in self.totValues:
            val.setFont(valfont)
            val.setAlignment(Qt.AlignRight)
            val.setMinimumHeight(30)


        self.recieptGroup.setLayout(recieptGrid)
        vbox.addWidget(self.recieptGroup)
        vbox.addStretch()
        self.recieptContainer.setLayout(vbox)

    #******************************************** Logic Functions ************************************
    def exit_pro(self):
        choice = QMessageBox.question(self, "Exit!", "Do you want to close this program?",
                                      QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if choice == QMessageBox.Yes:
            sys.exit()

    def selectedItem(self, btnItem, lblprice, lblquantity ):
        if btnItem.isChecked() == True:
            item = btnItem.text()
            price = float(lblprice.text())
            quantity = float(lblquantity.text())
            try:
                text = self.scrReciept.text()
                self.scrReciept.setText(text+"\n{}\t{}\t\t{}\t{}".format(
                    item, price, quantity, str(price * quantity)
                ))
                text2 = float(self.scrTotal.text())
                self.scrTotal.setText(str(text2 + (price * quantity)))
            except Exception as e:
                print(e)

    def getTotalAction(self):
        try:
            total = float(self.scrTotal.text())
            discount = total * 0.05
            valueBeforeTax = total - discount
            VATTax = valueBeforeTax * 0.14
            valueAfterTax = valueBeforeTax + VATTax
            self.scrDiscount.setText(str(round(discount,2)))
            self.scrVAT.setText(str(round(VATTax, 2)))
            self.scrNetValue.setText(str(round(valueAfterTax, 2)))
        except Exception as e:
            print(e)

    def getInvoiceAction(self):
        try:
            total = float(self.scrTotal.text())
            discount = total * 0.05
            valueBeforeTax = total - discount
            VATTax = valueBeforeTax * 0.14
            valueAfterTax = valueBeforeTax + VATTax
            self.totalValue.setText(str(total))
            self.disValue.setText(str(round(discount, 2)))
            self.VATValue.setText(str(round(VATTax, 2)))
            self.netValue.setText(str(round(valueAfterTax, 2)))
        except Exception as e:
            print(e)

    def newTransaction(self):
        checkers = [
            self.chkShrimp, self.chkFish, self.chkBeef, self.chkChicken,
            self.chkBeefShawarma, self.chkChickenShawarma, self.chkMeatRiceNuts,
            self.chkMeatKofta, self.chkVegetables,
            self.chkCappuccino, self.chkEspresso, self.chkTurkishCoffee, self.chkBackTea,
            self.chkGreenTea, self.chkOrangeJuice, self.chkLemonade,
            self.chGreenApple, self.chkWaterBottle
        ]
        for checker in checkers:
            if checker.isChecked() == True:
                checker.setChecked(False)
        self.scrReciept.clear()

        quantities = [
            self.QCappuccino, self.QEspresso, self.QTurkishCoffee, self.QBlackTea,
            self.QGreenTea, self.QOrangeJuice, self.QLemonade,
            self.QGreenApple, self.QWaterBottle,
            self.QShrimp, self.QFish, self.QBeef, self.QChicken,
            self.QBeefShawarma, self.QChickenShawarma, self.QMeatRiceNuts,
            self.QMeatKofta, self.QVegetables
        ]
        for quantity in quantities:
            quantity.setText("0")
        try:
            self.scrTotal.setText("0")
            self.totalValue.setText("0")
            self.disValue.setText("0")
            self.VATValue.setText("0")
            self.netValue.setText("0")
            self.scrDiscount.setText("0")
            self.scrVAT.setText("0")
            self.scrNetValue.setText("0")
            time = QTime.currentTime()
            date = QDate.currentDate()
            invNumber = QDateTime.currentDateTime()
            self.recTime.clear()
            self.recDate.clear()
            self.recNumberValue.clear()
            self.recTime.setText("الوقت:" + time.toString(Qt.DefaultLocaleLongDate))
            self.recDate.setText("التاريخ: " + date.toString(Qt.ISODate))
            RestaurantBillingSystem.invoice_no += 1
            self.recNumberValue.setText(invNumber.toString(Qt.ISODate) + " " + str(RestaurantBillingSystem.invoice_no))

        except Exception as e:
            print(e)


def main():
    app = QApplication(sys.argv)
    win = RestaurantBillingSystem()
    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

