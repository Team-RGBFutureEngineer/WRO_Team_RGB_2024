// Pin definitions
const int encoderPinA = 2; // Encoder A channel connected to pin 2
const int encoderPinB = 3; // Encoder B channel connected to pin 3

// Variables
volatile int encoderPosition = 0;
volatile int lastEncoded = 0;

const int pulsesPerRevolution = 8192; // Encoder pulses per revolution
const float wheelDiameter = 6.88;     // Diameter of the wheel in cm

// Calculate wheel circumference
const float wheelCircumference = PI * wheelDiameter;

// Calculate distance per pulse
const float distancePerPulse = wheelCircumference / pulsesPerRevolution;

void setup() {
  // Set up encoder pins as inputs
  pinMode(encoderPinA, INPUT);
  pinMode(encoderPinB, INPUT);

  // Enable pull-up resistors
  digitalWrite(encoderPinA, HIGH);
  digitalWrite(encoderPinB, HIGH);

  // Attach interrupts to the encoder pins
  attachInterrupt(digitalPinToInterrupt(encoderPinA), updateEncoder, CHANGE);
  attachInterrupt(digitalPinToInterrupt(encoderPinB), updateEncoder, CHANGE);

  // Start serial communication
  Serial.begin(9600);
}

void loop() {
  // Calculate the distance traveled in centimeters
  float distance = encoderPosition * distancePerPulse;

  // Print the distance
  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.println(" cm");

  // Add a small delay to avoid flooding the serial output
  delay(100);
}

void updateEncoder() {
  int MSB = digitalRead(encoderPinA); // MSB = most significant bit
  int LSB = digitalRead(encoderPinB); // LSB = least significant bit

  int encoded = (MSB << 1) | LSB; // Combine the two values into a single integer
  int sum = (lastEncoded << 2) | encoded; // Calculate the difference
  lastEncoded = encoded;

  // Determine the direction and increment/decrement the position
  if (sum == 0b1101 || sum == 0b0100 || sum == 0b0010 || sum == 0b1011) encoderPosition++;
  if (sum == 0b1110 || sum == 0b0111 || sum == 0b0001 || sum == 0b1000) encoderPosition--;
}
