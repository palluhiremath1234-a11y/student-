from student import student_details

def test_student():
    result = student_details(
        "Pallavi",
        "01FE25BCA012",
        "KLE College",
        "Hubli"
    )

    assert result["name"] == "Pallavi"
    assert result["usn"] == "01FE25BCA012"
    assert result["college"] == "KLE College"
    assert result["city"] == "Hubli"