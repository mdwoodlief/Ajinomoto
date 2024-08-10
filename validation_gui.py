import sys
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QComboBox,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
)


def get_validation_method(drug_name, spec_limit, method):
    method = method.lower()

    if method == "identification":
        validation_details = {
            "Test Function": "Identification",
            "Validation Characteristics": "Specificity",
            "Acceptance Criteria": "The method must be able to distinguish the analyte from all potential interfering substances.",
        }

    elif method == "assay":
        validation_details = {
            "Test Function": "Assay",
            "Validation Characteristics": (
                "Accuracy, Precision (Repeatability and Intermediate Precision), "
                "Specificity, Detection Limit, Quantitation Limit, Linearity, and Range"
            ),
            "Acceptance Criteria": (
                "Accuracy: % recovery should be within 98.0% to 102.0%."
                "Precision: % RSD should not exceed 2.0%."
                "Specificity: The analyte peak should be well-resolved from other components."
                "Linearity: Correlation coefficient (r) should be ≥ 0.999 over the working range."
                "Range: 80% to 120% of the nominal concentration."
            ),
        }

    elif method == "impurities":
        validation_details = {
            "Test Function": "Impurities",
            "Validation Characteristics": (
                "Specificity, Quantitation Limit, Linearity, Accuracy, and Precision"
            ),
            "Acceptance Criteria": (
                "Specificity: Impurities should be well-resolved from the main analyte."
                "Quantitation Limit: The lowest amount of impurity should be detected with acceptable precision."
                "Linearity: Correlation coefficient (r) should be ≥ 0.99."
                "Accuracy: % recovery of impurities should be within 80.0% to 120.0%."
                "Precision: % RSD for impurities should not exceed 10.0%."
            ),
        }

    elif method == "dissolution":
        validation_details = {
            "Test Function": "Dissolution",
            "Validation Characteristics": (
                "Accuracy, Precision, Specificity, Linearity, and Range"
            ),
            "Acceptance Criteria": (
                "Accuracy: % recovery should be within 95.0% to 105.0%."
                "Precision: % RSD should not exceed 5.0%."
                "Specificity: The method should clearly separate the drug substance from excipients."
                "Linearity: Correlation coefficient (r) should be ≥ 0.995 over the working range."
                "Range: Typically 75% to 125% of the label claim."
            ),
        }

    else:
        return "The desired method is not recognized. Please select from 'identification', 'assay', 'impurities', or 'dissolution'."

    # Format output message
    output_message = (
        f"Drug Product: {drug_name}\n"
        f"Component Specification Limit: {spec_limit}\n"
        f"Test Function: {validation_details['Test Function']}\n"
        f"Validation Characteristics: {validation_details['Validation Characteristics']}\n"
        f"Acceptance Criteria:\n{validation_details['Acceptance Criteria']}"
    )

    return output_message


class ValidationApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Drug Product Validation")

        # Create layout
        layout = QVBoxLayout()

        # Drug product name input
        self.drug_name_label = QLabel("Drug Product Name:")
        self.drug_name_input = QLineEdit()
        layout.addWidget(self.drug_name_label)
        layout.addWidget(self.drug_name_input)

        # Component specification limit input
        self.spec_limit_label = QLabel("Component Specification Limit:")
        self.spec_limit_input = QLineEdit()
        layout.addWidget(self.spec_limit_label)
        layout.addWidget(self.spec_limit_input)

        # Validation method selection
        self.method_label = QLabel("Validation Method:")
        self.method_combo = QComboBox()
        self.method_combo.addItems(
            ["Identification", "Assay", "Impurities", "Dissolution"]
        )
        layout.addWidget(self.method_label)
        layout.addWidget(self.method_combo)

        # Submit button
        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.show_validation_details)
        layout.addWidget(self.submit_button)

        # Output text area
        self.output_area = QTextEdit()
        self.output_area.setReadOnly(True)
        layout.addWidget(self.output_area)

        self.setLayout(layout)

    def show_validation_details(self):
        drug_name = self.drug_name_input.text()
        spec_limit = self.spec_limit_input.text()
        method = self.method_combo.currentText()

        validation_method = get_validation_method(drug_name, spec_limit, method)
        self.output_area.setText(validation_method)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    validation_app = ValidationApp()
    validation_app.show()

    sys.exit(app.exec())
