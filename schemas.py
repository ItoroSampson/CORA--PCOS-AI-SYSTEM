from pydantic import BaseModel, Field


class PatientData(BaseModel):
    Age: int = Field(gt=12, lt=60)
    BMI: float = Field(gt=14, lt=40)
    Menstrual_Irregularity: bool
    Testosterone_Level: float
    Antral_Follicle_Count: int = Field(gt=1, lt=50)


if __name__ == "__main__":
    try:
        data = PatientData(
            Age=24,
            BMI=15.5,
            Menstrual_Irregularity=0,
            Testosterone_Level=45.0,
            Antral_Follicle_Count=3,
        )
        patient = data.model_dump()
        print("Validation successful")
    except Exception as e:
        print(f"Data Error: {e}")
