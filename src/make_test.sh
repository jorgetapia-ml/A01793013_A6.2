log_file="hostelry.txt"
paths=(
    "hostelry_module/customer.py"
    "hostelry_module/reservation.py"
    "hostelry_module/hotel.py"
)

for i in "${!paths[@]}"; do
    path="${paths[$i]}"
    echo Testing with $path
    
    echo "----------------PyLint-------------------" | tee -a "$log_file"
    pylint $path | tee -a "$log_file"

    echo "----------------flake8-------------------" | tee -a "$log_file"
    flake8 $path | tee -a "$log_file"
    echo "flake8 finish" | tee -a "$log_file"
done

echo "----------------Coverage-------------------" | tee -a "$log_file"
coverage run -m unittest hotel_unitest.py | tee -a "$log_file"
coverage report | tee -a "$log_file"