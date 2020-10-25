playing=True

while(playing):
  doyouwanttoplay= input("Type 'N' if you don't want to play games, type anything else to continue \n")

  if(doyouwanttoplay == 'N'):
    break
  else:
    print("Pick a game to play (type 1, 2, 3, or 4):")
    answer = input("1) Country/Continent Game \n2) Mad Libs Game \n3) Calculator Game \n4) Color Mixing Game \n")

    if(int(answer) == 1):
        print("Welcome to the Country/Continent Game!")
        gamemode= input("Instructions: You can either choose to 1) type in countries and see what continent they're on or 2) play our multiple choice game! (type '1' or '2') \n ")

        #create country/continent list
        Asia = ["Afghanistan", "Armenia", "Azerbaijan", "Bahrain", "Bangladesh", "Bhutan", "Brunei", "Cambodia", "China", "Cyprus", "Georgia", "India", "Indonesia",
        "Iran", "Israel", "Japan", "Jordan", "Kazakhstan", "Kuwait", "Kyrgyzstan", "Laos", "Lebanon", "Malaysia", "Maldives", "Mongolia", "Myanmar", "Nepal", "North Korea",
        "Oman", "Pakistan", "Palestine", "Philippines", "Qatar", "Russia", "Saudi Arabia", "Singapore", "South Korea", "Sri Lanka", "Syria", "Taiwan", "Tajikistan", "Thailand",
        "Timor-Leste", "Turkey", "Turkmenistan", "United Arab Emirates", "Uzbekistan", "Vietnam", "Yemen"]
        NorthAmerica = ["Antigua and Barbuda", "Bahamas", "Barbados", "Belize", "Canada", "Costa Rica", "Cuba", "Dominica", "Dominican Republic", "El Salvador", "Grenada",
        "Guatamala", "Haiti", "Honduras", "Jamaica", "Mexico", "Nicaragua", "Panama", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", "Trinidad and Tobago",
        "United States of America"]
        SouthAmerica = ["Argentina", "Bolivia","Brazil","Chile","Colombia","Ecuador","Guyana","Paraguay","Peru","Suriname","Uruguay","Venezuela"]
        Europe=["Albania", "Andorra", "Austria", "Belarus","Belgium","Bosnia and Herzegovina", "Bulgaria", "Croatia", "Cyprus", "Czechia", "Denmark", "Estonia", "Finland", "France", "Germany",
        "Greece", "Hungary", "Iceland", "Ireland", "Italy", "Kosovo", "Latvia", "Liechtenstein", "Lithuania", "Luxembourg","Malta", "Moldova", "Monaco", "Montenegro", "Netherlands",
        "North Macedonia", "Norway","Poland", "Portugal", "Romania", "San Marino", "Serbia", "Slovakia","Slovenia", "Spain", "Sweden", "Switzerland", "Ukraine", "United Kingdom", "Vatican City"]
        AustraliaOceania=["Australia", "Fiji","Kiribati","Marshall Islands","Micronesia","Nauru","New Zealand","Palau","Papua New Guinea","Samoa","Solomon Islands","Tonga","Tuvalu","Vanuatu"]
        Africa=["Algeria","Angola","Benin","Botswana","Burkina Faso","Burundi","Cabo Verde","Cameroon","Central African Republic","Chad","Comoros","Democratic Republic of the Congo",
        "Republic of the Congo", "Cote d'Ivoire","Djibouti","Egypt","Equatorial Guinea","Eritrea","Eswatini","Ethiopia","Gabon","Gambia","Ghana","Guinea","Guinea-Bissau","Kenya","Lesotho",
        "Liberia", "Libya","Madagascar","Malawi","Mauritania","Mauritius","Morocco","Mozambique","Namibia","Niger","Nigeria", "Rwanda", "Sao Tome and Principe", "Senegal",
        "Saychelles", "Sierra Leone"," Somalia", "South Africa", "South Sudan", "Sudan", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"]


        if(gamemode=="1"):
          print("Congrats, you have picked to type in countries! Please type names with correct capitalization and no abbreviations (dependent territories are not included in this game).")
          playing1 = True
          while(playing1):
            Notfound = True
            while(Notfound):
                countryIn= input("Type in a country \n")
                for country in Asia:
                    if(countryIn == country):
                        print("Asia")
                        Notfound = False
                        break
                for country in NorthAmerica:
                    if(countryIn == country):
                        print("North America")
                        Notfound = False
                        break
                for country in SouthAmerica:
                    if(countryIn == country):
                        print("South America")
                        Notfound = False
                        break
                for country in Europe:
                    if(countryIn == country):
                        print("Europe")
                        Notfound = False
                        break
                for country in AustraliaOceania:
                    if(countryIn == country):
                        print("Australia/Oceania")
                        Notfound = False
                        break
                for country in Africa:
                    if(countryIn == country):
                        print("Africa")
                        Notfound = False
                        break
                if(Notfound):
                  playingBoolean= input("Could not find country, type anything to play again or 'N' to exit this game\n")
                  if(playingBoolean == 'N'):
                      playing1 = False
                      break
            playingBoolean= input("Type anything to play again or 'N' to exit this game \n")
            if(playingBoolean == 'N'):
              playing1 = False
              break

        elif(gamemode=="2"):
            print("Congrats, you have picked to play the multiple choice game! Please only type the number of the answer you chose.")
            score=0

            answer1= input("Where is Sierra Leone? Is it 1 Asia 2 Europe 3 Africa \n")
            if(answer1=="3"):
                score+=1
            print("The correct answer is 3")

            answer2= input("Where is Belarus? Is it 1 South America 2 Europe 3 Africa \n")
            if(answer2=="1"):
                score+=1
            print("The correct answer is 1")

            answer3= input("Where is Brunei? Is it 1 Asia 2 South America 3 Australia/Oceania \n")
            if(answer3=="1"):
                score+=1
            print("The correct answer is 1")

            print("Your score is "+ str(score)+" out of 3, congrats!")
    elif(int(answer) == 2):
        color= input("Enter a color: ")
        plural_noun= input("Enter a plural noun: ")
        celbrity= input("Enter a celebrity: ")

        print("Roses are "+color)
        print(plural_noun+" are blue")
        print("I love "+celbrity)

        fruit= input("Entrez un fruit:")
        number= input("Entrez un nombre:")
        month= input("Entrez un month:")
        adjective=input("Entrez un adjective:")
        nationality=input("Entrez un nationalite:")
        print("Aujourd'hui nous allons au restaurant "+fruit)
        print("C'est le "+number+month+" mon annivensaine.")
        print("Je suis trés "+adjective+" paroe que nous allons manger la nourrtine "+nationality)

        adj= input("Enter an adjective: ")
        noun=input("Write a noun: ")
        noun2=input("Write another noun: ")
        noun3=input("Write a 3rd noun: ")
        noun4=input("Write a fourth noun: ")
        preposition=input("Enter a proposition: ")
        verb=input("Enter a verb: ")
        print("Nice to meet you, where you been?")
        print("I could show you "+adj+ " things")
        print(noun+","+noun2+","+noun3+","+noun4)
        print("Saw you "+preposition+ " and I "+verb)
        print("Oh my god "+verb+" at that "+noun4)
        print("You "+verb+" like my next "+noun3)
        print(noun2+"'s a game, wanna "+verb+"? Ayy")
        print("by Trailor Swift")
    elif(int(answer) == 3):
            # Python program for simple calculator 
          
        # Function to add two numbers  
        def add(num1, num2): 
            return num1 + num2 
          
        # Function to subtract two numbers  
        def subtract(num1, num2): 
            return num1 - num2 
          
        # Function to multiply two numbers 
        def multiply(num1, num2): 
            return num1 * num2 
          
        # Function to divide two numbers 
        def divide(num1, num2):
          if(num2 == "0"):
            print("Not a real number") 
            return num1
          return num1 / num2 
          
        print("Please select operation -\n" 
                "1. Add\n" 
                "2. Subtract\n" 
                "3. Multiply\n" 
                "4. Divide\n") 
          
          
        # Take input from the user  
        select = int(input("Select operations form 1, 2, 3, 4 :")) 
          
        number_1 = int(input("Enter first number: ")) 
        number_2 = int(input("Enter second number: ")) 
        if select >=4:
            print("Invalid input")
        elif select == 1: 
            print(number_1, "+", number_2, "=", 
                            add(number_1, number_2)) 
          
        elif select == 2: 
            print(number_1, "-", number_2, "=", 
                            subtract(number_1, number_2)) 
          
        elif select == 3: 
            print(number_1, "*", number_2, "=", 
                            multiply(number_1, number_2)) 
          
        elif select == 4:
          if(number_2 == 0):
            print("Invalid input") 
          else:
            print(number_1, "/", number_2, "=", 
                            divide(number_1, number_2)) 
        else: 
            print("Invalid input")
    elif(int(answer)==4):
        print ("Welcome to color mixing game!")
        print ("You can type it any two colors on the list : blue, red, yellow, green, orange, purple")

        color1 = input("Enter your first color ")
        color2 = input ("Enter your second color ")

        if (color1 == "red"):
          if (color2 == "blue"):
            print (color1 + " and " + color2 + " make purple!")
          elif (color2 == "yellow"):
            print (color1 + " and " + color2 + "make orange!")
          elif (color2 == "green"):
            print (color1 + " and " + color2 + " make brown!")
          elif (color2 == "orange"):
            print (color1 + " and " + color2 + " make red-orange")
          elif (color2 == "purple"):
            print (color1 + " and " + color2 + " make magenta")
          elif (color2 == "red"):
            print (color1 + " and " + color2 + " don't change the color!")
        elif (color1 == "orange"):
          if (color2 == "red"):
            print (color1 + " and " + color2 + " make red-orange!")
          elif (color2 == "yellow"):
            print (color1 + " and " + color2 + " make amber!")
          elif (color2 == "green"):
            print (color1 + " and " + color2 + " make brown")
          elif (color2 == "blue"):
            print (color1 + " and " + color2 + " make brown!")
          elif (color2 == "purple"):
            print (color1 + " and " + color2 + " make brown!")
          elif (color2 == "ornage"):
            print (color1 + " and " + color2 + " don't change the color!")
        elif (color1 == "blue"):
          if (color2 == "red"):
            print (color1 + " and " + color2 + " make purple!")
          elif (color2 == "yellow"):
            print (color1 + " and " + color2 + " make green!")
          elif (color2 == "green"):
            print (color1 + " and " + color2 + " make blue green!")
          elif (color2 == "purple"):
            print (color1 + " and " + color2 + " make blue-violet!")
          elif (color2 == "orange"):
            print (color1 + " and " + color2 + " make brown")
          elif (color2 == "blue"):
            print (color1 + " and " + color2 + " don't change the color!")
        elif (color1 == "yellow"):
          if (color2 == "red"):
            print (color1 + " and " + color2 + " make orange!")
          elif (color2 == "blue"):
            print (color1 + " and " + color2 + " make green!")
          elif (color2 == "green"):
            print (color1 + " and " + color2 + " make lime!")
          elif (color2 == "purple"):
            print (color1 + " and " + color2 + " make brown!")
          elif (color2 == "orange"):
            print (color1 + " and " + color2 + " make light orange!")
          elif (color2 == "yellow"):
            print (color1 + " and " + color2 + " don't change the color!")
        elif (color1 == "green"):
          if (color2 == "red"):
            print (color1 + " and " + color2 + " make brown!")
          elif (color2 == "blue"):
            print (color1 + " and " + color2 + " make blue green!")
          elif (color2 == "yellow"):
            print (color1 + " and " + color2 + " make lime!")
          elif (color2 == "purple"):
            print (color1 + " and " + color2 + " make brown!")
          elif (color2 == "orange"):
            print (color1 + " and " + color2 + " make brown!")
          elif (color2 == "green"):
            print (color1 + " and " + color2 + " don't change the color!")
        elif (color1 == "purple"):
          if (color2 == "green" or "yellow" or "orange"):
            print (color1 + " and " + color2 + " make brown!")
          elif (color2 == "blue"):
            print (color1 + " and " + color2 + " make blue-violet!")
          elif (color2 == "red"):
            print (color1 + " and " + color2 + " make magenta")
          elif (color2 == "purple"):
            print (color1 + " and " + color2 + " don't change color!")  
        else:
          print ("You did not write a valid color")
    else:
        print("Invalid game mode")

