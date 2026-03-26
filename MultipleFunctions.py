{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "042886b5-1813-496e-96a4-6af3055709e0",
   "metadata": {},
   "outputs": [],
   "source": [
    "class multiplefunction():\n",
    "        def Subfields():\n",
    "          Lists= [\"Machine Learning\",\"Neural Networks\",\"Vision\",\"Robotics\",\"Speech Processing\",\"Natural Language Processing\"]\n",
    "          print(\"Sub-fields in AI are:\")\n",
    "          for subfield in Lists:\n",
    "              print(subfield)\n",
    "        def OddEven():\n",
    "          Num= int(input(\"Enter a number:\"))\n",
    "          if(Num%2==0):\n",
    "            print(Num,\"is Even number\")\n",
    "          else:\n",
    "            print(Num,\"is Odd number\") \n",
    "        def Elegible():\n",
    "          Gender=input(\"Your Gender:\")\n",
    "          Age=int(input(\"Your Age:\"))\n",
    "          if (Gender == \"Male\" and Age >= 21):\n",
    "            print (\"Elegible\")\n",
    "          elif (Gender == \"Female\" and Age >= 18):\n",
    "            print (\"Elegible\")\n",
    "          else: \n",
    "            print (\"Not Eligible\")\n",
    "        def percentage():\n",
    "          sub1= int(input(\"Subject1=\"))\n",
    "          sub2= int(input(\"Subject2=\"))\n",
    "          sub3= int(input(\"Subject3=\"))\n",
    "          sub4= int(input(\"Subject4=\"))\n",
    "          sub5= int(input(\"Subject5=\"))\n",
    "          totalmarks= sub1+sub2+sub3+sub4+sub5\n",
    "          print(\"Total:\",totalmarks)\n",
    "          avg= (totalmarks / 500)*100\n",
    "          print(\"Percentage:\",avg)\n",
    "        def triangle():\n",
    "          height= int(input(\"Height:\"))\n",
    "          base= int(input(\"Base:\"))\n",
    "          print(\"Area formula: (Height*Base)/2\")\n",
    "          Area= (height*base)/2\n",
    "          print(\"Area of triangle:\",Area)\n",
    "          side1=int(input(\"Side1:\"))\n",
    "          side2=int(input(\"Side2:\"))\n",
    "          base=int(input(\"Base:\"))\n",
    "          print(\"Perimeter formula: Side1+Side2+Base\")\n",
    "          Perimeter= side1+side2+base\n",
    "          print(\"Perimeter of Triangle:\",Perimeter)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "525c2f73-2570-4846-a356-aeb74c24d8c0",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
