model1 = sequential()
model1.compile()
model1.fit()
model2 = sequential()
model2.compile()
model2.fit()
model3 = sequential()
model3.compile()
model3.fit()

prob1 = model1.predict_prob()
prob2 = model2.predict_prob()
prob3 = model3.predict_prob()
final_prob = (prob1 + prob2 + prob3)/3