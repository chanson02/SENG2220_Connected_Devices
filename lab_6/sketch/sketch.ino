int temp_pin = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600); //baud // bits per second

}

void loop() {
  // put your main code here, to run repeatedly:
  int reading = analogRead(temp_pin);
  float voltage = reading * 5.0 / 1024;
  float temperatureC = (voltage - 0.5) * 100;
  float temperatureF = (temperatureC * 9 / 5) + 32;
//  Serial.print(voltage); Serial.println(" volts");
//  Serial.print(temperatureF); Serial.println(" degrees");
  Serial.println(temperatureF);
  delay(500);
}
