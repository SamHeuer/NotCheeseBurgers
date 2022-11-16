from tkinter import *
import customtkinter
import tkintermapview
from PIL import Image, ImageTk

root=Tk()

def fun():
    print("Wait for Not Cheeseburgers 2.0")

def orderConfirmed():
    global billVal,orderPriceLabel
    orderPriceLabel.place_forget()
    if billVal.get()>0 :
        orderPriceLabel.configure(text= "Order Confirmed")
    else:
        orderPriceLabel.configure(text= "Invalid Input")
        billVal=IntVar(0)
    orderPriceLabel.place(relx=0.25,rely=0.95)

def chooseMargarita():
    global billVal, orderPriceLabel
    orderPriceLabel.place_forget()
    billVal.set(249 +billVal.get())
    orderPriceLabel.configure(text= ("Bill : ₹ " + str(billVal.get())))
    orderPriceLabel.place(relx=0.25,rely=0.95)

def choosePepporoni():
    global billVal, orderPriceLabel
    billVal.set(299 +billVal.get())
    orderPriceLabel.place_forget()
    orderPriceLabel.configure(text= ("Bill : ₹ " + str(billVal.get())))
    orderPriceLabel.place(relx=0.25,rely=0.95)

def chooseChicken():
    global billVal, orderPriceLabel
    billVal.set(349 +billVal.get())
    orderPriceLabel.place_forget()
    orderPriceLabel.configure(text= ("Bill : ₹ " + str(billVal.get())))
    orderPriceLabel.place(relx=0.25,rely=0.95)

def chooseVegetarian():
    global billVal, orderPriceLabel
    billVal.set(349 +billVal.get())
    orderPriceLabel.configure(text= ("Bill : ₹ " + str(billVal.get())))
    orderPriceLabel.place(relx=0.25,rely=0.95)

# utility Functions:
def configAllButtons():
    global homeButton,orderButton,mapButton,profileButton,content
    for widget in content.winfo_children():
        widget.pack_forget()
    homeButton.configure(image=homeIcon,fg_color="#ffffff",hover_color="#ffffff",command=openHome)
    orderButton.configure(image=orderIcon,fg_color="#ffffff",hover_color="#ffffff",command=openOrder)
    mapButton.configure(image=locationIcon,fg_color="#ffffff",hover_color="#ffffff",command=openLocation)
    profileButton.configure(image=accountIcon,fg_color="#ffffff",hover_color="#ffffff",command=openAccount)

def openHome():
    configAllButtons()
    homeButton.configure(image=homeIconSelected,fg_color="#e67e00",hover_color="#e67e00",command=openHome)
    setHomeContent()
    
def openLocation():
    configAllButtons()
    mapButton.configure(image=locationIconSelected,fg_color="#e67e00",hover_color="#e67e00",command=openLocation)
    setLocationContent()
    
def openOrder():
    configAllButtons()
    orderButton.configure(image=orderIconSelected,fg_color="#e67e00",hover_color="#e67e00",command=openOrder)
    setOrderContent()

def openAccount():
    configAllButtons()
    profileButton.configure(image=accountIconSelected,fg_color="#e67e00",hover_color="#e67e00",command=openAccount)
    setProfileContent()
    
def setFooter():
    # Footers buttons 
    global homeButton,orderButton,mapButton,profileButton
    
    homeButton = customtkinter.CTkButton(footer,text="",image=homeIcon,fg_color="#ffffff",hover_color="#ffffff",width=240 ,command=openHome)
    homeButton.grid(row=0,column= 0)
    mapButton = customtkinter.CTkButton(footer,text="",image=locationIcon,fg_color="#ffffff",hover_color="#ffffff",width=240 ,command=openLocation)
    mapButton.grid(row=0,column= 1)
    orderButton = customtkinter.CTkButton(footer,text="",image=orderIcon,fg_color="#ffffff",hover_color="#ffffff",width=240,command=openOrder)
    orderButton.grid(row=0,column= 2)
    profileButton = customtkinter.CTkButton(footer,text="",image=accountIcon,fg_color="#ffffff",hover_color="#ffffff",width=240 ,command=openAccount)
    profileButton.grid(row=0,column= 3)
    content.pack(fill='both')
    footer.pack(fill='both', side='bottom')

def mapLocationChanger(*args):
    map_widget.set_address(location_var.get())

def setLocationContent():
    global location_var,map_widget
    
    # Placing Map
    mapTools = Canvas(content,bg="white",width=480,highlightthickness=0)
    map = Canvas(content,bg="white", width=480,highlightthickness=0)
    mapTools.pack(fill='y',side="left")
    map.pack(fill='y', side='right')
    map_widget = tkintermapview.TkinterMapView(map, corner_radius=45,width=480,height=636,bg_color="white")
    map_widget.set_position(31.2560, 75.7051) 
    map_widget.set_zoom(14)
    map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)
    map_widget.pack()
    
    Label(mapTools,text="We Are Right By Your Home!",font=("inter bold", 25),fg="#d87130",bg="white").place(relx=0.5,rely=0.2,anchor= CENTER)
    Label(mapTools,text="Drop Your Address To Confirm!",font=("inter bold", 15),fg="grey",bg="white").place(relx=0.5,rely=0.27,anchor= CENTER)

    # Search Box container
    mapToolsContainter = customtkinter.CTkFrame(mapTools, corner_radius=10,fg_color="#d87130",bg_color="white",width=240,height=200)
    mapToolsContainter.place(relx=0.5, rely=0.5,anchor= CENTER)
    
    # Search Box
    searchBox = customtkinter.CTkEntry(mapToolsContainter,textvariable = location_var,fg_color="white", text_font=('Helvectica',10,'normal'),text_color="black", width=200)
    searchBox.focus_force()
    searchBox.place(relx=0.5, rely=0.5,anchor= CENTER)

    searchBox.bind('<Return>',mapLocationChanger) 

def setHomeContent():

    pizzaGalleryCanvas=Canvas(content,width=980,height=337,highlightthickness=0)
    pizzaGalleryCanvas.pack(fill='x',side='top')

    coverimage = Image.open("./Media/Home/pizzaGallery1.jpg")
    homePageCoverImage = ImageTk.PhotoImage(coverimage)
    homePageCoverImageLabel = Label(pizzaGalleryCanvas,image=homePageCoverImage)
    homePageCoverImageLabel.image = homePageCoverImage

    homePageCoverImageLabel.place(x=0, y=0)

    homeCardCanvas=Canvas(content,bg="white",width=980,height=300,highlightthickness=0)
    homeCardCanvas.pack(fill='both',side='bottom')
    
    homeCardWidgetContainer1=customtkinter.CTkFrame(homeCardCanvas, corner_radius=0,fg_color="white",bg_color="white",width=325,height=300)
    homeCardWidgetContainer1.pack(fill='y',side='left')

    homeCardWidgetContainer2=customtkinter.CTkFrame(homeCardCanvas, corner_radius=0,fg_color="white",bg_color="white",width=325,height=300)
    homeCardWidgetContainer2.pack(fill='y',side='left')

    homeCardWidgetContainer3=customtkinter.CTkFrame(homeCardCanvas, corner_radius=0,fg_color="white",bg_color="white",width=325,height=300)
    homeCardWidgetContainer3.pack(fill='y',side='left')
    
    homeCardWidgetContainer1Box=customtkinter.CTkFrame(homeCardWidgetContainer1, corner_radius=10,fg_color="grey",bg_color="white",width=300,height=290)
    homeCardWidgetContainer1Box.place(relx=0.5,rely=0.5,anchor="center")

    widgetLeftHeadingLabel=Label(homeCardWidgetContainer1Box,text="DELIVERY!",font=("inter bold", 25,"underline"),fg="black",bg="grey")
    widgetLeftHeadingLabel.place(relx=0.5,rely=0.15,anchor= CENTER)

    homePageMsg="Did you know we saved almost four thousand gallons of gas last year by delivering on bikes? And we began piloting an ebike program for our delivery team. Good for you, good for earth!"
    widgetLeftContentLabel=Message(homeCardWidgetContainer1Box,text=homePageMsg,font=("inter bold", 13),fg="white",bg="grey")
    widgetLeftContentLabel.place(relx=0.5,rely=0.5,anchor= "center")

    
    widgetImage = ImageTk.PhotoImage(Image.open("./Media/Home/homeWidget.png"))
    
    homeCardWidgetContainer2Box=customtkinter.CTkFrame(homeCardWidgetContainer2, corner_radius=10,fg_color="black",bg_color="white",width=300,height=290)
    homeCardWidgetContainer2Box.place(relx=0.5,rely=0.5,anchor="center")
    
    widgetImageLabel=customtkinter.CTkLabel(homeCardWidgetContainer2Box,image=widgetImage, text="")
    widgetImageLabel.image=widgetImage
    widgetImageLabel.place(relx=0.5,rely=0.5,anchor="center")

    homeCardWidgetContainer3Box=customtkinter.CTkFrame(homeCardWidgetContainer3, corner_radius=10,fg_color="#94B49F",bg_color="white",width=300,height=290)
    homeCardWidgetContainer3Box.place(relx=0.5,rely=0.5,anchor="center")
    
    widgetRightHeadingLabel=Label(homeCardWidgetContainer3Box,text="ORDER NOW!",font=("inter bold", 25,"underline"),fg="black",bg="#94B49F")
    widgetRightHeadingLabel.place(relx=0.5,rely=0.15,anchor= CENTER)

    firstline="Mon To Thurs 4 PM - 12 AM"
    secondline="Fri 11 AM - 2 AM"
    thirdline="Sat 11 AM - 3 AM"
    fourthline="Sun 11 AM - 12 AM"
    
    widgetRightContentLabel1=Label(homeCardWidgetContainer3Box,text=firstline,font=("inter bold", 13),fg="white",bg="#94B49F")
    widgetRightContentLabel1.place(relx=0.5,rely=0.3,anchor= "center")
    
    widgetRightContentLabel2=Label(homeCardWidgetContainer3Box,text=secondline,font=("inter bold", 13),fg="white",bg="#94B49F")
    widgetRightContentLabel2.place(relx=0.5,rely=0.4,anchor= "center")
    
    widgetRightContentLabel3=Label(homeCardWidgetContainer3Box,text=thirdline,font=("inter bold", 13),fg="white",bg="#94B49F")
    widgetRightContentLabel3.place(relx=0.5,rely=0.5,anchor= "center")
    
    widgetRightContentLabel4=Label(homeCardWidgetContainer3Box,text=fourthline,font=("inter bold", 13),fg="white",bg="#94B49F")
    widgetRightContentLabel4.place(relx=0.5,rely=0.6,anchor= "center")
    
def nextButton():
    global counter,imgLabel,prev,next,gallery
    counter+=1
    imgLabel.pack_forget()
    imgLabel.config(image=gallery[counter])
    imgLabel.image=gallery[counter]
    imgLabel.place(y=0,x=0)
    prev.state=NORMAL
    if counter==4:
        counter=0

def prevButton():
    global counter,imgLabel,prev,next,gallery
    next.state=NORMAL
    counter-=1
    imgLabel.pack_forget()
    imgLabel.config(image=gallery[counter])
    imgLabel.place(y=0,x=0)
    if counter==0:
        counter=2

def setOrderContent():
    global gallery,imgLabel,prev,next,orderPriceLabel
    
    orderShowCase =Canvas(content,bg="white",height=637,width=480,highlightthickness=0)
    orderShowCase.pack(fill="both",side="left")

    orderForm = Canvas(content,bg="white",height=637,width=480,highlightthickness=0)
    orderForm.pack(fill="both",side="left")
    
    img1 = ImageTk.PhotoImage(Image.open("./Media/Order/orderImage1.jpg").resize((480,637)),Image.Resampling.LANCZOS)
    img2 = ImageTk.PhotoImage(Image.open("./Media/Order/orderImage2.jpg").resize((480,637)),Image.Resampling.LANCZOS)
    img3 = ImageTk.PhotoImage(Image.open("./Media/Order/orderImage3.jpg").resize((480,637)),Image.Resampling.LANCZOS)
    img4 = ImageTk.PhotoImage(Image.open("./Media/Order/orderImage4.jpg").resize((480,637)),Image.Resampling.LANCZOS)
    img5 = ImageTk.PhotoImage(Image.open("./Media/Order/orderImage5.jpg").resize((480,637)),Image.Resampling.LANCZOS)

    gallery=[img1,img2,img3,img4,img5]

    imgContainer=Canvas(orderShowCase,width=480,height=637,bg="white")
    imgContainer.place(relx=0,rely=0)

    imgLabel=Label(imgContainer,image=gallery[counter],borderwidth=0)
    imgLabel.image=gallery[counter]
    imgLabel.place(y=0,x=0)
    
    prev = customtkinter.CTkButton(orderShowCase,width=5,corner_radius=3,height=25, text="<",bg_color="grey",fg_color="grey",hover_color="grey", border_width=0,command=prevButton,state=DISABLED)
    prev.place(relx=0,rely=0.5)
    next= customtkinter.CTkButton(orderShowCase,width=5,corner_radius=3, text=">",bg_color="grey",fg_color="grey",hover_color="grey", border_width=0, command=nextButton,height=25,highlightthickness=0)
    next.place(relx=0.96,rely=0.5)

    # order form
    heading=customtkinter.CTkLabel(orderForm,text="ORDER NOW!",corner_radius=8, text_font=("inter bold", 25),fg_color="#688f4e",bg_color="white",text_color="white")
    heading.place(relx=0.25,rely=0.025)

    deliveryTypeCanvas=Canvas(orderForm,bg="white",height=10,width=400,highlightthickness=0)
    deliveryTypeCanvas.place(relx=0.38,rely=0.1)
    deliveryType=IntVar()
    deliveryRadioButton=customtkinter.CTkRadioButton(deliveryTypeCanvas,text="Delivery",variable=deliveryType,text_color="black",fg_color="#688f4e",hover_color="#688f4e",value=1,bg="white")
    deliveryRadioButton.pack(side="left",padx=(0,10))
    pickUpRadioButton=customtkinter.CTkRadioButton(deliveryTypeCanvas,text="Pick Up",variable=deliveryType,value=2,text_color="black",fg_color="#688f4e",hover_color="#688f4e",bg="white")
    pickUpRadioButton.pack(side="right")

    pizzaButtonCanvas=Canvas(orderForm,bg="white",height=550,width=400,background="white",highlightthickness=0)
    pizzaButtonCanvas.place(relx=0.09,rely=0.15)
    
    # clickable Order Images

    orderPizzaImg1 = ImageTk.PhotoImage(Image.open("./Media/Order/orderPizzaImg1.jpg").resize((400,120)),Image.Resampling.LANCZOS)
    orderPizzaImg2 = ImageTk.PhotoImage(Image.open("./Media/Order/orderPizzaImg2.jpg").resize((400,120)),Image.Resampling.LANCZOS)
    orderPizzaImg3 = ImageTk.PhotoImage(Image.open("./Media/Order/orderPizzaImg3.jpg").resize((400,120)),Image.Resampling.LANCZOS)
    orderPizzaImg4 = ImageTk.PhotoImage(Image.open("./Media/Order/orderPizzaImg4.jpg").resize((400,120)),Image.Resampling.LANCZOS)

    pizzaButton1=customtkinter.CTkButton(pizzaButtonCanvas,width=400,corner_radius=8, text="",image=orderPizzaImg1,bg_color="white",fg_color="white",hover_color="white", border_width=0, command=chooseMargarita,height=100,highlightthickness=0)
    pizzaButton1.pack(fill="both",side="top")

    pizzaButton2=customtkinter.CTkButton(pizzaButtonCanvas,width=400,corner_radius=8, text="",image=orderPizzaImg2,bg_color="white",fg_color="white",hover_color="white", border_width=0, command=choosePepporoni,height=100,highlightthickness=0)
    pizzaButton2.pack(fill="both",side="top")

    pizzaButton3=customtkinter.CTkButton(pizzaButtonCanvas,width=400,corner_radius=8, text="",image=orderPizzaImg3,bg_color="white",fg_color="white",hover_color="white", border_width=0, command=chooseChicken,height=100,highlightthickness=0)
    pizzaButton3.pack(fill="both",side="top")

    pizzaButton4=customtkinter.CTkButton(pizzaButtonCanvas,width=400,corner_radius=8, text="",image=orderPizzaImg4,bg_color="white",fg_color="white",hover_color="white", border_width=0, command=chooseVegetarian,height=100,highlightthickness=0)
    pizzaButton4.pack(fill="both",side="top")

    orderPriceLabel=customtkinter.CTkButton(orderForm,height=15,width=250,corner_radius=8,text="Bill :", text_font=("inter bold", 12),fg_color="#688f4e",bg_color="white",text_color="white",hover_color="#466d2c",command=orderConfirmed)
    orderPriceLabel.place(relx=0.25,rely=0.95)

def setProfileContent():
    profileCoverCanvas=Canvas(content,bg="white",height=634,width=399,highlightthickness=0)
    profileCoverCanvas.pack(fill="both",side="right")

    profileCoverImage=ImageTk.PhotoImage(Image.open("./Media/Profile/profileCover.jpg"),Image.Resampling.LANCZOS)

    profileCoverLabel=Label(profileCoverCanvas,image=profileCoverImage,height=634,width=399,borderwidth=0)
    profileCoverLabel.image=profileCoverImage
    profileCoverLabel.pack(fill="both",anchor="center")

    profileToolsContainer=Canvas(content,bg="white",height=634,highlightthickness=0)
    profileToolsContainer.pack(fill="both")

    #  Greetings 

    greetingImage=ImageTk.PhotoImage(Image.open("./Media/Profile/profileGreeting.jpg").resize((300,67)),Image.Resampling.LANCZOS)
    greetingImageLabel=Label(profileToolsContainer,text="",image=greetingImage,borderwidth=0,highlightthickness=0)
    greetingImageLabel.image=greetingImage
    greetingImageLabel.place(x=0,y=0)
    greetingLabel=customtkinter.CTkLabel(profileToolsContainer,text="Hi "+ username_var.get()+" !", text_font=("inter bold", 25),fg_color="#cb763f",bg_color="#cb763f",text_color="white")
    greetingLabel.place(relx=0.023,rely=0.023)

    #  Profile related options
     
    profileSettingsContainer=Canvas(profileToolsContainer,bg="white",height=510,width=475,highlightthickness=0)
    profileSettingsContainer.place(relx=0.04,rely=0.15)

    profileSettingsLabel=customtkinter.CTkLabel( profileSettingsContainer,fg_color="white", bg_color="white",text="• Account Settings •",text_font=("Helvectica bold", 10),text_color="grey",width=475,height=30)
    profileSettingsLabel.pack(fill="both",side="top")

    changeAccountSettings=customtkinter.CTkButton(profileSettingsContainer,width=475,corner_radius=8,bg_color="white",text_color="black",fg_color="white",hover_color="#cb763f", border_width=0, command=fun,height=30,text="Modify Account Settings",text_font=("helvectica bold", 10))
    changeAccountSettings.pack(fill="both",side="top")

    modifyAddress=customtkinter.CTkButton(profileSettingsContainer,width=475,corner_radius=8,bg_color="white",text_color="black",fg_color="white",hover_color="#cb763f", border_width=0, command=fun,height=30,text="Modify Addresses",text_font=("helvectica bold", 10))
    modifyAddress.pack(fill="both",side="top")

    changeAccountSettings=customtkinter.CTkButton(profileSettingsContainer,width=475,corner_radius=8,bg_color="white",text_color="black",fg_color="white",hover_color="#cb763f", border_width=0, command=fun,height=30,text="Modify Account Settings",text_font=("helvectica bold", 10))
    changeAccountSettings.pack(fill="both",side="top")

    # Order related options

    orderLabel=customtkinter.CTkLabel( profileSettingsContainer,fg_color="white", bg_color="white",text="• Orders •",text_font=("Helvectica bold", 10),text_color="grey",width=475,height=30)
    orderLabel.pack(fill="both",side="top")

    trackOrder=customtkinter.CTkButton(profileSettingsContainer,width=475,corner_radius=8,bg_color="white",text_color="black",fg_color="white",hover_color="#cb763f", border_width=0, command=fun,height=30,text="Track Your Order",text_font=("helvectica bold", 10))
    trackOrder.pack(fill="both",side="top")

    orderHistory=customtkinter.CTkButton(profileSettingsContainer,width=475,corner_radius=8,bg_color="white",text_color="black",fg_color="white",hover_color="#cb763f", border_width=0, command=fun,height=30,text="Order History",text_font=("helvectica bold", 10))
    orderHistory.pack(fill="both",side="top")

    favourites=customtkinter.CTkButton(profileSettingsContainer,width=475,corner_radius=8,bg_color="white",text_color="black",fg_color="white",hover_color="#cb763f", border_width=0, command=fun,height=30,text="My Favourites",text_font=("helvectica bold", 10))
    favourites.pack(fill="both",side="top")

    #  Payment related options

    paymentLabel=customtkinter.CTkLabel( profileSettingsContainer,fg_color="white", bg_color="white",text="• Payments •",text_font=("Helvectica bold", 10),text_color="grey",width=475,height=30)
    paymentLabel.pack(fill="both",side="top")

    savedCards=customtkinter.CTkButton(profileSettingsContainer,width=475,corner_radius=8,bg_color="white",text_color="black",fg_color="white",hover_color="#cb763f", border_width=0, command=fun,height=30,text="Saved Cards",text_font=("helvectica bold", 10))
    savedCards.pack(fill="both",side="top")

    invoices=customtkinter.CTkButton(profileSettingsContainer,width=475,corner_radius=8,bg_color="white",text_color="black",fg_color="white",hover_color="#cb763f", border_width=0, command=fun,height=30,text="Invoices",text_font=("helvectica bold", 10))
    invoices.pack(fill="both",side="top")

    tax=customtkinter.CTkButton(profileSettingsContainer,width=475,corner_radius=8,bg_color="white",text_color="black",fg_color="white",hover_color="#cb763f", border_width=0, command=fun,height=30,text="Tax",text_font=("helvectica bold", 10))
    tax.pack(fill="both",side="top")

    spacer=customtkinter.CTkLabel( profileSettingsContainer,fg_color="white", bg_color="white",text="",text_font=("Helvectica bold", 10),text_color="grey",width=475,height=30)
    spacer.pack(fill="both",side="top")

    # sign out

    signOut=customtkinter.CTkButton(profileSettingsContainer,width=300,corner_radius=8,bg_color="white",text_color="white",fg_color="#cb763f",hover_color="#a9541d", border_width=0, command=root.destroy,height=30,text="Sign Out",text_font=("helvectica bold", 10))
    signOut.pack(fill="y",side="top")



def signupbutton(*args):
    global warning,username_var,password_var
    if ''==password_var.get() or  ''==username_var.get() in password_var.get() or ' ' in username_var.get():
        warning.grid_forget()
        warning.place(relx=0.70,rely=0.8)
        warning.configure(text="Warning : Enter Valid Input!",text_font=("Helvectica bold", 10),text_color="#d87130")
    else:
        for widget in root.winfo_children():
            widget.pack_forget()
            widget.grid_forget()
            widget.place_forget()
        setFooter()
        openHome()

def mainApp():
    root.title("Not CheeseBurgers")
    root.geometry("960x667")
    root.minsize(width=960, height=667)
    root.maxsize(width=960, height=667)
    root.configure(background="white")
    root.rowconfigure(0,weight=1)
    root.columnconfigure(0,weight=1)
    root.iconbitmap("./Media/Icons/icon.ico")

def mainSignUpContent():

    #  adding cover-image

    test = ImageTk.PhotoImage(Image.open("./Media/SignUp/coverImage.jpg"))
    coverimagelabel = Label(root,image=test,height=668,width=480,highlightthickness=0)
    coverimagelabel.image=test
    coverimagelabel.pack(fill="both",side="left")

    # setting up signup canvas
    
    signupWindow= Canvas(root, height=668, width=480,bg="#ffffff",highlightthickness=0)
    signupWindow.place(x=480, y=0)
    signupWindow.rowconfigure(0,weight=4)
    spacer=Label(signupWindow,text="", bg="#ffffff",padx=0,font=("Helvectica bold", 150))
    spacer.grid(row=0,column=0,rowspan=8)

    # signup text-contents

    signupGreetingLabel = Label(signupWindow, text="Cheeseburgers Suck! But Our Pizzas Don't",font=("Helvectica bold", 18), bg="#ffffff", padx=0)  
    signupGreetingLabel.grid(row=9,column=0)
    
    signupForm= Canvas(signupWindow,bg="#ffffff",highlightthickness=0)
    signupForm.grid(row=10,column=0,padx=0)
    signupForm.columnconfigure(1,weight=2)

    spacer1=Label(signupForm,text="", bg="#ffffff",padx=0)
    spacer2=Label(signupForm,text="", bg="#ffffff",padx=0)
    spacer1.grid(row=0,column=0)
    spacer2.grid(row=1,column=0)

    usernameLabel= Label(signupForm,text="Username :",font=("Helvectica bold", 10), bg="#ffffff",padx=0)
    usernameLabel.grid(row=3,column=0)

    usernameInputField= customtkinter.CTkEntry(signupForm,textvariable = username_var,fg_color="white", text_font=('Helvectica',10,'normal'),text_color="black")
    usernameInputField.grid(row=3,column=1,columnspan=2,padx=(10,0))
    usernameInputField.focus_force()
    
    passwordLabel= Label(signupForm,text="Password :",font=("Helvectica bold", 10), bg="#ffffff",padx=0)
    passwordLabel.grid(row=4,column=0)
    
    passwordInputField= customtkinter.CTkEntry(signupForm,textvariable = password_var,fg_color="white", text_font=('Helvectica',10,'normal'),text_color="black",show="*")
    passwordInputField.grid(row=4,column=1,columnspan=2,padx=(10,0),pady=(5,5))
    passwordInputField.bind('<Return>',signupbutton)

    # whitespacing

    spacer3=Label(signupForm,text="", bg="#ffffff",padx=0)
    spacer4=Label(signupForm,text="", bg="#ffffff",padx=0)
    spacer3.grid(row=5,column=0)
    spacer4.grid(row=6,column=0)

    signinbutton = customtkinter.CTkButton(signupForm,text="Sign In",fg_color="#fdad5c",text_color="#ffffff",hover_color="#e67e00" ,command=signupbutton)
    signinbutton.grid(row=7,column= 1) 
    
    # more white spacing 

    warning=customtkinter.CTkLabel(signupForm,text="",corner_radius=8, fg_color="white",bg_color="white",pady=20)
    warning.grid(row=8,column=1)

# creating footer icons
homeIcon = PhotoImage(file="./Media/Icons/home.png")
locationIcon = PhotoImage(file="./Media/Icons/location.png")
orderIcon = PhotoImage(file="./Media/Icons/order.png")
accountIcon = PhotoImage(file="./Media/Icons/account.png")

#  creating selected-footer icons
homeIconSelected = PhotoImage(file="./Media/Icons/selected-home.png")
locationIconSelected = PhotoImage(file="./Media/Icons/selected-location.png")
orderIconSelected = PhotoImage(file="./Media/Icons/selected-order.png")
accountIconSelected = PhotoImage(file="./Media/Icons/selected-account.png") 

# Global Buttons
homeButton=customtkinter.CTkButton()
mapButton=customtkinter.CTkButton()
orderButton=customtkinter.CTkButton()
profileButton=customtkinter.CTkButton()

# Internal Buttons
next=customtkinter.CTkButton()
prev=customtkinter.CTkButton()

orderPriceLabel=customtkinter.CTkLabel()
warning=customtkinter.CTkLabel()
content = Canvas(root,bg="white")
footer = Canvas(root,bg="white", height=30)

imgContainer=Canvas()
gallery=[]
counter=0

# Order counters
billVal=IntVar(0)
imgLabel=Label()

username_var=StringVar()
password_var=StringVar()
location_var=StringVar()
mainApp()
mainSignUpContent()

root.mainloop()