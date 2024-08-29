//Reading Values of Colors
// Pin definitions
const int S0 = 4;   // S0 pin
const int S1 = 5;   // S1 pin
const int S2 = 6;   // S2 pin
const int S3 = 7;   // S3 pin
const int sensorOut = 8; // OUT pin

// Variables to store frequency values for each color
unsigned long redFrequency = 0;
unsigned long greenFrequency = 0;
unsigned long blueFrequency = 0;

void setup() {
  // Set the control pins as outputs
  pinMode(S0, OUTPUT);
  pinMode(S1, OUTPUT);
  pinMode(S2, OUTPUT);
  pinMode(S3, OUTPUT);

  // Set the sensor output as input
  pinMode(sensorOut, INPUT);

  // Set frequency scaling to 20% (S0 HIGH, S1 LOW)
  digitalWrite(S0, HIGH);
  digitalWrite(S1, LOW);

  // Start serial communication for debugging
  Serial.begin(9600);
}

void loop() {
  // Set S2 and S3 to read red frequency
  digitalWrite(S2, LOW);
  digitalWrite(S3, LOW);
  redFrequency = pulseIn(sensorOut, LOW);
  delay(100); // Add a small delay to stabilize readings

  // Set S2 and S3 to read green frequency
  digitalWrite(S2, HIGH);
  digitalWrite(S3, HIGH);
  greenFrequency = pulseIn(sensorOut, LOW);
  delay(100); // Add a small delay to stabilize readings

  // Set S2 and S3 to read blue frequency
  digitalWrite(S2, LOW);
  digitalWrite(S3, HIGH);
  blueFrequency = pulseIn(sensorOut, LOW);
  delay(100); // Add a small delay to stabilize readings

  // Print the color frequencies to the Serial Monitor
  Serial.print("Red: ");
  Serial.print(redFrequency);
  Serial.print(" Green: ");
  Serial.print(greenFrequency);
  Serial.print(" Blue: ");
  Serial.println(blueFrequency);

  // Add a delay between readings
  delay(500);
}
                                                                        
