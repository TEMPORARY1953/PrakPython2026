C = type('C', (), {'Q-Q!': 42, '__init__': lambda s, v: setattr(s, 'Q-Q!', v), '__str__': lambda s: f"C({getattr(s,'Q-Q!')})"})
print(C(7))
