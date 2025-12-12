from django.shortcuts import render

def calculate_power(request):
    power = None
    if request.method == "POST":
        current = float(request.POST.get("current"))   # I
        resistance = float(request.POST.get("resistance"))  # R
        power = (current ** 2) * resistance            # P = I² × R
        print(f"Current: {current} A, Resistance: {resistance} Ω, Power: {power:.2f} W")

    return render(request, 'mathapp/math.html', {'Power': power})