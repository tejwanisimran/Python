from sklearn.metrics import r2_score

def main():
    y_actual = [3,4,2,4,5]                  # Y
    y_predicted = [2.8,3.2,3.6,4.0,4.4]     # Yp

    r2 = r2_score(y_actual,y_predicted)

    print("Actual Values are : ",y_actual)
    print("Predicted Values are : ",y_predicted)

    print("R square Value is : ",r2)        # 0.307
    
if __name__ == "__main__":
    main()