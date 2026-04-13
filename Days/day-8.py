# * REVISION 
# 1. string (done)
# 2. list (done old things and learned nested list)
# 3. tuple (done old things and learned nested tuple)
# 4. numerical data (done)
# 5. oprations 

# NESTED LIST (NEW CONCEPT)
'''
🧠 NESTED LISTS (from zero → strong)
🔹 What is a Nested List?

👉 A nested list is simply:

a list inside another list

🔥 Example
a = [[1, 2], [3, 4]]

👉 Structure:

element 0 → [1, 2]
element 1 → [3, 4]
🧠 Visual Understanding
a = [
      [1, 2],
      [3, 4]
    ]

👉 Think of it like rows

🔹 Accessing Elements (VERY IMPORTANT)
Step 1: Access inner list
a[0]   # → [1, 2]
Step 2: Access element inside
a[0][0]   # → 1
a[1][1]   # → 4
🔥 Full Mapping
a[0][0] → 1
a[0][1] → 2
a[1][0] → 3
a[1][1] → 4
⚡ Rule

👉 First index → which list
👉 Second index → which element inside that list

🎴 Practice Card 1

Q: What will be the output?

a = [[10, 20], [30, 40]]
print(a[1][0])

Try yourself 👇 (don’t scroll fast)

✅ Answer

👉 30

🔹 Modifying Nested Lists
a = [[1, 2], [3, 4]]
a[0][1] = 100

👉 Now:

[[1, 100], [3, 4]]
🎴 Practice Card 2

Q: Output?

a = [[5, 6], [7, 8]]
a[1][1] = 0
print(a)
✅ Answer

👉 [[5, 6], [7, 0]]

🔹 Important Concept (connect with reference)
a = [[1, 2], [3, 4]]
b = a
b[0][0] = 99

👉 BOTH change:

[[99, 2], [3, 4]]
⚠️ Why?

👉 Because:

b = a → same reference
nested elements also linked
🔥 Common Mistake

People think:
👉 inner list is separate

Reality:
👉 it’s still part of same memory when referenced

🎴 Practice Card 3 (important)

Q: What will be output?

a = [[1, 2], [3, 4]]
b = a[:]
b[0][0] = 50

print(a)

⚠️ This is tricky — shallow copy concept

Try 👇 (don’t rush)

🧠 Big Insight (don’t skip)

👉 a[:] copies outer list only
👉 inner lists are still shared

✅ Answer

👉 [[50, 2], [3, 4]] ❗
'''


# NESTED TUPLE
'''
🧠 NESTED TUPLE (CORE)
🔹 What is it?

👉 Tuple inside tuple

a = ((1,2),(3,4))
🔹 Accessing (same as list)
a[0]      # (1,2)
a[0][1]   # 2
🔥 Practice Card 1
a = ((10,20),(30,40))
print(a[1][0])

Answer 👇

🔥 Now Important Twist
❌ You CANNOT modify tuple
a = ((1,2),(3,4))
a[0][0] = 100   # ❌ ERROR
🔥 But… same trick as list
Tuple with list inside
a = ((1,2), [3,4])
a[1][0] = 100

👉 This works ✅

🔥 Practice Card 2
a = ((1,2), [3,4])
a[1][1] = 200

print(a)

Answer 👇

🔥 Multi-level nested
a = ((1,2),(3,(4,5)))
🔥 Practice Card 3
a = ((1,2),(3,(4,5)))

print(a[1][1][1])

Answer 👇

⚠️ Critical Rule
Case	Allowed?
Change tuple element	❌
Change list inside tuple	✅
Access nested	✅
🔥 Final Boss (like list)
a = ((1,2), [3,(4,5)])

a[1][1] = (9,9)

print(a)
'''
n = 5
for i in range(1, n+1):        # Outer loop → rows
    for j in range(1, i+1):    # Inner loop → columns per row
        print(j, end=" ")
    print()                     # Move to next row
