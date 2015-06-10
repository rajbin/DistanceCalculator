from Tour import Tour

def displayOption():
    firstTour = Tour("New York, NY", "Lansing, MI")
    secondTour = Tour("Oakland, CA")
    thirdTour = Tour("Sacramento, CA", "Oakland, CA")

    print("""\nFirst Tour:{0}
Second Tour:{1}
Third Tour:{2}\n""".format(firstTour, secondTour, thirdTour))

    print("First tour distances:\n\tDriving: {0} km;\n\tBiking: {1} km;\n\tWalking: {2} km".format(
    round(firstTour.getDistance("driving")/1000), round(firstTour.getDistance('bicycling')/1000),
    round(firstTour.getDistance('walking')/1000)))

    print("\nSecond tour distances:\n\tDriving: {0} km;\n\tBiking: {1} km;\n\tWalking: {2} km".format(
    round(secondTour.getDistance("driving")/1000), round(secondTour.getDistance('bicycling')/1000),
    round(secondTour.getDistance('walking')/1000)))

    print("\nThird tour distances:\n\tDriving: {0} km;\n\tBiking: {1} km;\n\tWalking: {2} km".format(
    round(thirdTour.getDistance("driving")/1000), round(thirdTour.getDistance('bicycling')/1000),
    round(thirdTour.getDistance('walking')/1000)))

def main():
    displayOption()

main()