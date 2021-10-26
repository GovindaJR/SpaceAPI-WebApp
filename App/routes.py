from App import app
from flask import render_template, request
from App.apicalls import get_people_in_ISS, get_aurora_locations, get_aurora_images_info, get_aurora_image

# renders the home page
@app.route("/")
def home():
    return render_template("index.html")


# renders the International Space Station (ISS) route
@app.route("/iss")
def iss():
    # gets json data about all people in the ISS
    people_in_ISS = get_people_in_ISS()
    num_people = len(people_in_ISS)
    return render_template("iss.html", people=people_in_ISS, num_people=num_people)


@app.route("/aurora", methods=["GET","POST"])
def aurora():
    images = get_aurora_images_info()
    locations = get_aurora_locations()
    value = ""
    if request.method == "POST":
        # if the button is pressed, get image data and pass to template
        value = request.form.get("location_form")
        get_aurora_image(value)
        show_image= True
    else:
        show_image = False
    return render_template("aurora.html", locations=locations,
                           images=images,
                           show_image=show_image,
                           value=value)


if __name__ == "__main__":
    app.run(debug=True)
