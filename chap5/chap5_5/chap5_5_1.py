from pathlib import Path
path = Path()
for filepath in path.glob('*.py'):
  print(filepath)

  # chapごとにデレクトリーを変えてしまったので、できない様子。一読に抑える。