import os
import re

def parse_and_create():
    with open('/home/juan-mrtn/Documents/DavCore/DiccionariosEnBruto/codigo.md', 'r') as f:
        lines = f.read().splitlines()

    current_dir = None
    current_file = None
    in_code = False
    current_code = []
    
    for i, line in enumerate(lines):
        if line.startswith("Ubicación:") or line.startswith("Ubicación sugerida:"):
            current_dir = line.split(":", 1)[1].strip()
            
        elif line.startswith("Archivo"):
            parts = line.split(":", 1)
            if len(parts) >= 2:
                current_file = parts[1].strip()
                
        elif line.strip() == "Python" and current_file:
            in_code = True
            current_code = []
            
        elif in_code:
            if not current_code and line.strip() == "":
                continue
                
            current_code.append(line)
            
            # Check for termination
            is_end = False
            if current_file == "ayuda.py":
                if line.strip().endswith(")") or line.strip() == "":
                    # Let's peek ahead to see if next non-empty line starts with uppercase text
                    next_non_empty = None
                    for j in range(i+1, len(lines)):
                        if lines[j].strip():
                            next_non_empty = lines[j].strip()
                            break
                    if next_non_empty and not next_non_empty.startswith("#") and not next_non_empty.startswith("def") and not next_non_empty.startswith("print"):
                        is_end = True
            else:
                if line.strip() == "}":
                    is_end = True
                    
            if is_end:
                in_code = False
                
                # Write to file
                if current_dir and current_file:
                    rel_dir = current_dir
                    if rel_dir.startswith("tickets/DAV_Diccionario/"):
                        rel_dir = rel_dir.replace("tickets/DAV_Diccionario/", "")
                    
                    if rel_dir.startswith("PartWorkbench"):
                        rel_dir = rel_dir.replace("PartWorkbench", "PartWorkBench")
                    
                    full_dir = os.path.join("/home/juan-mrtn/Documents/DavCore/DiccionariosEnBruto", rel_dir)
                    os.makedirs(full_dir, exist_ok=True)
                    
                    full_path = os.path.join(full_dir, current_file)
                    print(f"Writing {full_path}")
                    with open(full_path, 'w') as out_f:
                        out_f.write("\n".join(current_code) + "\n")
                
                current_file = None
                current_code = []

if __name__ == "__main__":
    parse_and_create()
