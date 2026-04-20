from sklearn.metrics import r2_score

def main():
    y_actual = [3,4,2,4,5]                  # Y
    y_predicted = [1.8,1.2,3.6,1.0,2.4]     # Yp

    r2 = r2_score(y_actual,y_predicted)

    print("Actual Values are : ",y_actual)
    print("Predicted Values are : ",y_predicted)

    print("R square Value is : ",r2)        # -4.307
    
if __name__ == "__main__":
    main()