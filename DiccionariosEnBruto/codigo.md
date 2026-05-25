I am providing you with a Markdown file that contains Python code blocks for FreeCAD voice command dictionaries. I need you to act as an automated file generator and create the exact directory and file structure described in the text.

Please follow these exact instructions:

1. **Root Directories:** Create two main root folders named `PartWorkbench` and `AssemblyWorkbench`.
2. **Subdirectories:** For each feature or ticket mentioned in the text, determine which root folder it belongs to based on the context. Create a subfolder for each feature inside its corresponding root folder. Use `snake_case` for the subfolder names (e.g., `PartWorkbench/ellipsoid/`, `AssemblyWorkbench/create_joint_angle/`).
3. **File Creation:** Inside every subfolder, you must create exactly two files:
   - `<subfolder_name>.py` (e.g., `ellipsoid.py`, `create_joint_angle.py`): This file must contain the main dictionary and the lambda functions.
   - `ayuda.py`: This file must contain the `ayuda()` function.
4. **Code Population:** Extract the Python code blocks from the provided Markdown and paste them exactly as they are into their respective files. Ensure that the GNU General Public License (GPL) headers, comments, and relative imports (like `from .ayuda import ayuda`) are preserved perfectly.
5. **No Modifications:** Do not alter the Python code, the dictionary keys, or the FreeCAD API calls. Just parse the text and map the code to the file structure.

Please process the attached Markdown file and generate the complete workspace structure now.

¡Qué excelente proyecto el de la FCyT-UADER! Llevar accesibilidad al diseño 3D mediante comandos de voz tiene un tremendo impacto social, y está buenísimo que este desarrollo surja desde Entre Ríos. Organizar estos diccionarios en Python para el motor Vosk requiere un buen ojo analítico, y probar las importaciones directamente desde la consola de FreeCAD en tu entorno Ubuntu va a ser clave para ir puliendo el código de manera ágil.

Aquí tenés el procesamiento del primer ticket:
1. Análisis y corrección del ticket: Ellipsoid.txt

Al analizar los datos de la característica "Part Ellipsoid", detecté detalles importantes a ajustar según las convenciones obligatorias y el comportamiento real del software:

    Script Nativo: El ticket presenta un script de Python completo para invocar la geometría. Como bien señalaste en tu descripción, esto es un error; la regla estricta del proyecto exige una lambda que invoque un comando nativo.

        Advertencia sobre la API de FreeCAD: La documentación oficial indica que el elipsoide se genera internamente desde la herramienta Part → Primitives. FreeCAD no posee un comando de interfaz nativo individual que sea Part_Ellipsoid (como sí ocurre con Part_Box). Para cumplir la norma estricta del diccionario DAV, escribiremos Gui.runCommand('Part_Ellipsoid', 0), pero te sugiero advertir al equipo que si no existe una macro o wrapper registrando ese comando específico en la interfaz, la llamada directa podría fallar.

    Requiere y Devuelve: El ticket lista parámetros paramétricos de los ejes, como Radius1 y Radius3, junto con ángulos como Angle1 y sus valores por defecto. En realidad, estos son atributos configurables del objeto sólido una vez creado, no precondiciones operativas. El verdadero requerimiento para ejecutar el comando es contar con un documento activo. Al ejecutarse exitosamente, el comando devuelve un objeto Part::Ellipsoid agregado a dicho documento activo.

    Clave de Voz: El ticket sugiere la frase "Elipsoide" sumando combinaciones de números. Para respetar la regla de normalización del motor (minúsculas, sin tildes y preferentemente una sola palabra), la clave se debe reducir y limpiar, quedando únicamente en 'elipsoide'.

2. Estructura y Código Python

Dado que el elipsoide es una primitiva geométrica, lo ideal es crear un subgrupo Primitives dentro del módulo PartWorkbench. Esta subcarpeta te servirá para agrupar en futuros tickets los comandos de esferas, cajas, cilindros y conos.

Ubicación: tickets/DAV_Diccionario/PartWorkbench/Primitives/

Archivo 1: Primitives.py
Python

# Copyright (C) 2026 El Equipo del Proyecto DAV
# Universidad Autónoma de Entre Ríos (UADER)
# Bajo la dirección de Guillermo Gerard y Gallo Fabricio David
#
# Este programa es software libre: usted puede redistribuirlo y/o modificarlo
# bajo los términos de la Licencia Pública General GNU tal como fue publicada
# por la Fundación para el Software Libre, en la versión 3 de la Licencia.
#
# Este programa se distribuye con la esperanza de que sea útil,
# pero SIN NINGUNA GARANTÍA; incluso sin la garantía implícita de
# MERCANTIBILIDAD o APTITUD PARA UN PROPÓSITO PARTICULAR. Consulte la
# Licencia Pública General GNU para más detalles.
#
# Deberías haber recibido una copia de la Licencia Pública General GNU
# junto con este programa. Si no es así, consulte <http://www.gnu.org/licenses/>.

import FreeCADGui as Gui

primitives = {
    'elipsoide': lambda: Gui.runCommand('Part_Ellipsoid', 0),
}

Archivo 2: ayuda.py
Python

# Copyright (C) 2026 El Equipo del Proyecto DAV
# Universidad Autónoma de Entre Ríos (UADER)
# Bajo la dirección de Guillermo Gerard y Gallo Fabricio David
#
# Este programa es software libre: usted puede redistribuirlo y/o modificarlo
# bajo los términos de la Licencia Pública General GNU tal como fue publicada
# por la Fundación para el Software Libre, en la versión 3 de la Licencia.
#
# Este programa se distribuye con la esperanza de que sea útil,
# pero SIN NINGUNA GARANTÍA; incluso sin la garantía implícita de
# MERCANTIBILIDAD o APTITUD PARA UN PROPÓSITO PARTICULAR. Consulte la
# Licencia Pública General GNU para más detalles.
#
# Deberías haber recibido una copia de la Licencia Pública General GNU
# junto con este programa. Si no es así, consulte <http://www.gnu.org/licenses/>.

def ayuda():
    print("=== Primitives ===")
    print("  elipsoide: Genera un elipsoide sólido paramétrico | Req: Un documento activo")

Esta estructura inicial deja el subgrupo completamente preparado para ir sumando los siguientes diccionarios. Quedo a disposición para procesar el próximo ticket.

 En este repositorio tengo los ejemplos de como deberian quedar los diccionarios

¡Recibido! Estuve analizando detalladamente los ejemplos del repositorio que subiste y me vienen bárbaro para ajustar exactamente el código a lo que espera el equipo.

Noté un par de cosas muy importantes en estos ejemplos que definen cómo vamos a trabajar de ahora en adelante:

    El uso de Scripts vs. Gui.runCommand para las primitivas: En el primer ticket (Ellipsoid), la norma estricta decía que debíamos usar Gui.runCommand, pero habíamos notado que FreeCAD no tiene un comando nativo individual para cada primitiva. Viendo tus ejemplos (como box.py o cylinder.py), veo que el equipo optó por la solución más robusta: crear una función interna (ej. _create_box()) que utiliza directamente la API de FreeCAD (App.activeDocument().addObject(...)). A partir de ahora, voy a adoptar este mismo enfoque para todas las primitivas y comandos que lo requieran, ya que garantiza que el comando de voz funcione perfectamente.

    Estructura de carpetas: Veo que están armando subcarpetas individuales (o por pequeños grupos) con su propio archivo .py y su ayuda.py.

    Organización de los Workbenches: Un detalle a tener en cuenta es que en los ejemplos que me pasaste, pusieron las primitivas (box, cylinder, circle) dentro de AssemblyWorkbench/. Como vos me indicaste que tenemos que armar PartWorkbench y AssemblyWorkbench por separado, me voy a encargar de que las primitivas que hagamos nosotros (como la hélice, la cuña o el elipsoide) queden correctamente ubicadas dentro de la carpeta del PartWorkbench.

Ya tengo el formato exacto en la cabeza. Pasame el contenido del próximo ticket de tu lista (por ejemplo, Explicacion_Part_Primitives.txt, FineTuning-Preferences.txt o Helix.txt) y te armo la carpeta, el diccionario y el ayuda.py tal cual los ejemplos. ¡Vamos de a uno así quedan impecables!

Antes de seguir te paso mas contexto importante

¡Excelente! Recibido el contexto.

El documento Explicacion_Part_Primitives.txt es un archivo de diseño y justificación muy importante. Nos confirma que las primitivas son el "diccionario base" de objetos 3D para el sistema de voz , y justifica perfectamente nuestra decisión técnica de usar los parámetros con la API interna de FreeCAD en lugar de la GUI , ya que los objetos conservan su naturaleza paramétrica y pueden ser editados dinámicamente luego. Al ser explicativo, no requiere que le armemos un .py propio, pero marca la pauta para cuando procesemos los tickets de Caja, Cilindro, etc. que te quedan en la lista.  

Para el ticket FineTuning-Preferences.txt, se trata de la configuración avanzada del sistema (Parameter Editor). Según la documentación de FreeCAD, el comando nativo subyacente que abre "Tools → Edit parameters" es Std_DlgParameter.  

Aquí tienes la estructura para este comando. Lo ideal es agruparlo en una subcarpeta dedicada a preferencias avanzadas.

Ubicación: tickets/DAV_Diccionario/PartWorkbench/finetuning/

Archivo 1: finetuning.py
Python

# Copyright (C) 2026 El Equipo del Proyecto DAV
# Universidad Autónoma de Entre Ríos (UADER)
# Bajo la dirección de Guillermo Gerard y Gallo Fabricio David
#
# Este programa es software libre: usted puede redistribuirlo y/o modificarlo
# bajo los términos de la Licencia Pública General GNU tal como fue publicada
# por la Fundación para el Software Libre, en la versión 3 de la Licencia.
#
# Este programa se distribuye con la esperanza de que sea útil,
# pero SIN NINGUNA GARANTÍA; incluso sin la garantía implícita de
# MERCANTIBILIDAD o APTITUD PARA UN PROPÓSITO PARTICULAR. Consulte la
# Licencia Pública General GNU para más detalles.
#
# Deberías haber recibido una copia de la Licencia Pública General GNU
# junto con este programa. Si no es así, consulte <http://www.gnu.org/licenses/>.

import FreeCADGui as Gui
from .ayuda import ayuda

fineTuning = {
    'fine tuning': lambda: Gui.runCommand('Std_DlgParameter', 0),
    'configuracion avanzada': lambda: Gui.runCommand('Std_DlgParameter', 0),
    'modificar parametros': lambda: Gui.runCommand('Std_DlgParameter', 0),
    'help': ayuda,
}

Archivo 2: ayuda.py
Python

# Copyright (C) 2026 El Equipo del Proyecto DAV
# Universidad Autónoma de Entre Ríos (UADER)
# Bajo la dirección de Guillermo Gerard y Gallo Fabricio David
#
# Este programa es software libre: usted puede redistribuirlo y/o modificarlo
# bajo los términos de la Licencia Pública General GNU tal como fue publicada
# por la Fundación para el Software Libre, en la versión 3 de la Licencia.
#
# Este programa se distribuye con la esperanza de que sea útil,
# pero SIN NINGUNA GARANTÍA; incluso sin la garantía implícita de
# MERCANTIBILIDAD o APTITUD PARA UN PROPÓSITO PARTICULAR. Consulte la
# Licencia Pública General GNU para más detalles.
#
# Deberías haber recibido una copia de la Licencia Pública General GNU
# junto con este programa. Si no es así, consulte <http://www.gnu.org/licenses/>.

def ayuda():
    print('Comandos disponibles en este nivel:')
    print('  fine tuning / configuracion avanzada - Abre el Parameter Editor para ajustes finos de FreeCAD.')
    print('         Requiere: Conocimientos básicos sobre parámetros internos ubicados en BaseApp/Preferences/.')
    print('         Nota: Permite modificar preferencias avanzadas no disponibles en el Preferences Editor estándar.')
    print('               Algunos cambios requieren reiniciar FreeCAD para aplicarse correctamente.')

Notas sobre la implementación:

    Elegí las claves de voz 'fine tuning', 'configuracion avanzada' y 'modificar parametros' basándome en tus sugerencias, ya que son limpias, no tienen tildes y se adaptan perfectamente a las exigencias de Vosk.  

    Seguí la convención de importar el módulo de ayuda como en los ejemplos que me pasaste.

Pasame el siguiente ticket (como Helix.txt, ImportExport-Preferences.txt, etc.) y lo liquidamos de la misma manera.

Ticket Wedge

¡Perfecto! Al analizar el ticket del comando Part Wedge, vemos que permite generar una cuña sólida paramétrica definida por dos caras paralelas al plano XZ. Debido a que requiere múltiples parámetros de configuración para definir los vértices frontales y traseros (desde Xmin, Ymin, Zmin hasta X2max, Z2max), se lo considera el primitivo geométrico más complejo de configurar de todos.  

Para integrarlo correctamente al motor Vosk, la normalización estricta del diccionario nos obliga a quitar caracteres especiales y tildes de las palabras sugeridas, por lo que convertiremos "Cuña" directamente en la clave de voz 'cuna'. Además, en el ayuda.py dejaremos documentada la precondición geométrica clave: si la cara trasera se reduce a un punto o una arista, se obtienen formas piramidales o de cuña pura.  

A continuación, armamos la estructura y el código en su propia carpeta para mantener el estándar que venimos trabajando.

Ubicación: tickets/DAV_Diccionario/PartWorkbench/wedge/

Archivo 1: wedge.py
Python

# Copyright (C) 2026 El Equipo del Proyecto DAV
# Universidad Autónoma de Entre Ríos (UADER)
# Bajo la dirección de Guillermo Gerard y Gallo Fabricio David
#
# Este programa es software libre: usted puede redistribuirlo y/o modificarlo
# bajo los términos de la Licencia Pública General GNU tal como fue publicada
# por la Fundación para el Software Libre, en la versión 3 de la Licencia.
#
# Este programa se distribuye con la esperanza de que sea útil,
# pero SIN NINGUNA GARANTÍA; incluso sin la garantía implícita de
# MERCANTIBILIDAD o APTITUD PARA UN PROPÓSITO PARTICULAR. Consulte la
# Licencia Pública General GNU para más detalles.
#
# Deberías haber recibido una copia de la Licencia Pública General GNU
# junto con este programa. Si no es así, consulte <http://www.gnu.org/licenses/>.

import FreeCAD as App
from .ayuda import ayuda

def _create_wedge(xmin=0, ymin=0, zmin=0, x2min=2, z2min=2, xmax=10, ymax=15, zmax=10, x2max=8, z2max=8):
    doc = App.activeDocument()
    wedge = doc.addObject("Part::Wedge", "Wedge")
    wedge.Xmin = xmin
    wedge.Ymin = ymin
    wedge.Zmin = zmin
    wedge.X2min = x2min
    wedge.Z2min = z2min
    wedge.Xmax = xmax
    wedge.Ymax = ymax
    wedge.Zmax = zmax
    wedge.X2max = x2max
    wedge.Z2max = z2max
    doc.recompute()

wedge = {
    'cuna': lambda: _create_wedge(),
    'primitive wedge': lambda: _create_wedge(),
    'help': ayuda,
}

Archivo 2: ayuda.py
Python

# Copyright (C) 2026 El Equipo del Proyecto DAV
# Universidad Autónoma de Entre Ríos (UADER)
# Bajo la dirección de Guillermo Gerard y Gallo Fabricio David
#
# Este programa es software libre: usted puede redistribuirlo y/o modificarlo
# bajo los términos de la Licencia Pública General GNU tal como fue publicada
# por la Fundación para el Software Libre, en la versión 3 de la Licencia.
#
# Este programa se distribuye con la esperanza de que sea útil,
# pero SIN NINGUNA GARANTÍA; incluso sin la garantía implícita de
# MERCANTIBILIDAD o APTITUD PARA UN PROPÓSITO PARTICULAR. Consulte la
# Licencia Pública General GNU para más detalles.
#
# Deberías haber recibido una copia de la Licencia Pública General GNU
# junto con este programa. Si no es así, consulte <http://www.gnu.org/licenses/>.

def ayuda():
    print('Comandos disponibles en este nivel:')
    print('  cuna / primitive wedge - Crea una cuña sólida paramétrica (Part::Wedge).')
    print('         Requiere: Xmin, Ymin, Zmin (float) — vértice inferior de la cara frontal.')
    print('                   Xmax, Ymax, Zmax (float) — vértice superior de la cara trasera.')
    print('                   X2min, Z2min     (float) — vértice inferior de la cara trasera.')
    print('                   X2max, Z2max     (float) — vértice superior de la cara trasera.')
    print('         Nota: Es el primitivo más complejo de configurar.')
    print('               Si la cara trasera es un punto o una arista, se obtienen formas piramidales o de cuña pura.')
    print('               Disponible desde Part -> Primitives.')

El objeto ha quedado debidamente parametrizado siguiendo tu lógica funcional de API y ya está listo para ser invocado desde la consola mediante el diccionario. Pasame el próximo ticket de tu lista.

Ticket Helix

¡Recibido! Al analizar el ticket de Part Helix, notamos que se trata de otra primitiva geométrica generada internamente. En este caso, la hélice es un objeto de tipo alambre (wire), no sólido, pero que es fundamental para operaciones como el Sweep (barrido) o la creación de roscas.

Siguiendo las convenciones obligatorias y la lógica de normalización de Vosk, "Hélice" pierde la tilde y las mayúsculas, convirtiéndose en la clave de voz 'helice'. Además, configuraremos la función interna con los valores por defecto exactos que detalla el ticket en la sección <Requiere>.

Armaremos esto en su propia subcarpeta dentro de PartWorkbench, manteniendo la estructura individualizada que mostraste en tus ejemplos.

Ubicación: tickets/DAV_Diccionario/PartWorkbench/helix/

Archivo 1: helix.py
Python

# Copyright (C) 2026 El Equipo del Proyecto DAV
# Universidad Autónoma de Entre Ríos (UADER)
# Bajo la dirección de Guillermo Gerard y Gallo Fabricio David
#
# Este programa es software libre: usted puede redistribuirlo y/o modificarlo
# bajo los términos de la Licencia Pública General GNU tal como fue publicada
# por la Fundación para el Software Libre, en la versión 3 de la Licencia.
#
# Este programa se distribuye con la esperanza de que sea útil,
# pero SIN NINGUNA GARANTÍA; incluso sin la garantía implícita de
# MERCANTIBILIDAD o APTITUD PARA UN PROPÓSITO PARTICULAR. Consulte la
# Licencia Pública General GNU para más detalles.
#
# Deberías haber recibido una copia de la Licencia Pública General GNU
# junto con este programa. Si no es así, consulte <http://www.gnu.org/licenses/>.

import FreeCAD as App
from .ayuda import ayuda


def _create_helix(pitch=1.0, height=2.0, radius=1.0, angle=0.0):
    doc = App.activeDocument()
    helix = doc.addObject("Part::Helix", "Helix")
    helix.Pitch = pitch
    helix.Height = height
    helix.Radius = radius
    helix.Angle = angle
    doc.recompute()


helix = {
    'helice': lambda: _create_helix(),
    'primitive helix': lambda: _create_helix(),
    'help': ayuda,
}

Archivo 2: ayuda.py
Python

# Copyright (C) 2026 El Equipo del Proyecto DAV
# Universidad Autónoma de Entre Ríos (UADER)
# Bajo la dirección de Guillermo Gerard y Gallo Fabricio David
#
# Este programa es software libre: usted puede redistribuirlo y/o modificarlo
# bajo los términos de la Licencia Pública General GNU tal como fue publicada
# por la Fundación para el Software Libre, en la versión 3 de la Licencia.
#
# Este programa se distribuye con la esperanza de que sea útil,
# pero SIN NINGUNA GARANTÍA; incluso sin la garantía implícita de
# MERCANTIBILIDAD o APTITUD PARA UN PROPÓSITO PARTICULAR. Consulte la
# Licencia Pública General GNU para más detalles.
#
# Deberías haber recibido una copia de la Licencia Pública General GNU
# junto con este programa. Si no es así, consulte <http://www.gnu.org/licenses/>.


def ayuda():
    print('Comandos disponibles en este nivel:')
    print('  helice / primitive helix - Crea una hélice paramétrica (espiral en 3D).')
    print('         Requiere: Pitch  (float) — distancia entre vueltas consecutivas. Default: 1 mm.')
    print('                   Height (float) — altura total de la hélice. Default: 2 mm.')
    print('                   Radius (float) — radio inicial. Default: 1 mm.')
    print('                   Angle  (float) — ángulo cónico (0 = cilíndrica, >0 = cónica). Default: 0 grados.')
    print('         Nota: Genera una primitiva de alambre (wire), no sólida.')
    print('               Se usa frecuentemente como trayectoria para Sweep o roscas.')
    print('               Disponible desde Part -> Primitives.')

Con esto, la hélice ya queda integrada. Pasame el siguiente ticket cuando estés listo y lo procesamos.  

ticket new_sketch

¡Entendido! Analizando el ticket de Sketcher_NewSketch, nos topamos exactamente con uno de los errores frecuentes que mencionabas en las instrucciones de tu tarea.  

El ticket propone como script nativo la instanciación directa del objeto por API (obj = doc.addObject('Sketcher::SketchObject', 'Sketch')). Sin embargo, la descripción detalla explícitamente que la acción "abre el diálogo para editar perfiles 2D". Si usamos el método addObject, el diálogo para elegir el plano de orientación no se abrirá automáticamente en la interfaz. Por lo tanto, la solución correcta para este diccionario es usar el comando de GUI nativo: Gui.runCommand('Sketcher_NewSketch', 0).  

Por otro lado, aunque inicialmente me mencionaste que estabas armando los diccionarios de PartWorkbench y AssemblyWorkbench, la naturaleza de este comando es propia de los bocetos. Te armo la estructura sugerida para que la ubiques en SketcherWorkbench, o bien dentro del flujo de PartDesign si así lo tienen definido en su árbol de directorios.  

Las palabras sugeridas eran "Nuevo boceto", así que normalizamos la clave de voz a 'nuevo boceto'.  

Ubicación sugerida: tickets/DAV_Diccionario/SketcherWorkbench/new_sketch/

Archivo 1: new_sketch.py
Python

# Copyright (C) 2026 El Equipo del Proyecto DAV
# Universidad Autónoma de Entre Ríos (UADER)
# Bajo la dirección de Guillermo Gerard y Gallo Fabricio David
#
# Este programa es software libre: usted puede redistribuirlo y/o modificarlo
# bajo los términos de la Licencia Pública General GNU tal como fue publicada
# por la Fundación para el Software Libre, en la versión 3 de la Licencia.
#
# Este programa se distribuye con la esperanza de que sea útil,
# pero SIN NINGUNA GARANTÍA; incluso sin la garantía implícita de
# MERCANTIBILIDAD o APTITUD PARA UN PROPÓSITO PARTICULAR. Consulte la
# Licencia Pública General GNU para más detalles.
#
# Deberías haber recibido una copia de la Licencia Pública General GNU
# junto con este programa. Si no es así, consulte <http://www.gnu.org/licenses/>.

import FreeCADGui as Gui
from .ayuda import ayuda

new_sketch = {
    'nuevo boceto': lambda: Gui.runCommand('Sketcher_NewSketch', 0),
    'help': ayuda,
}

Archivo 2: ayuda.py
Python

# Copyright (C) 2026 El Equipo del Proyecto DAV
# Universidad Autónoma de Entre Ríos (UADER)
# Bajo la dirección de Guillermo Gerard y Gallo Fabricio David
#
# Este programa es software libre: usted puede redistribuirlo y/o modificarlo
# bajo los términos de la Licencia Pública General GNU tal como fue publicada
# por la Fundación para el Software Libre, en la versión 3 de la Licencia.
#
# Este programa se distribuye con la esperanza de que sea útil,
# pero SIN NINGUNA GARANTÍA; incluso sin la garantía implícita de
# MERCANTIBILIDAD o APTITUD PARA UN PROPÓSITO PARTICULAR. Consulte la
# Licencia Pública General GNU para más detalles.
#
# Deberías haber recibido una copia de la Licencia Pública General GNU
# junto con este programa. Si no es así, consulte <http://www.gnu.org/licenses/>.

def ayuda():
    print('Comandos disponibles en este nivel:')
    print('  nuevo boceto - Crea un nuevo boceto y abre el diálogo para editar perfiles 2D.')
    print('         Requiere: Seleccionar el plano de orientación (XY, XZ o YZ) desde el diálogo en pantalla.')
    print('         Devuelve: Un objeto tipo Sketch (Contenedor).')
    print('         Nota: Es la base necesaria para posteriores operaciones de extrusión o revolución.')

El diccionario quedó listo y documentado con sus precondiciones en la función de ayuda. Avisame cuál es el siguiente ticket en tu lista y seguimos.  

 ticket part_cross_section

¡Recibido! Al revisar el ticket de Part_CrossSections, nos encontramos con uno de los errores que me advertiste al principio: el campo del script nativo no tiene un comando válido, solo un comentario (# Genera múltiples secciones planas).

Como esta característica en FreeCAD abre un panel interactivo para que el usuario configure el eje, la cantidad y el espaciado de las secciones transversales, la forma correcta y robusta de invocarlo es a través del comando de interfaz gráfica nativo: Gui.runCommand('Part_CrossSections', 0).

Además, la sugerencia de voz era "Secciones transversales" + objeto. Para mantenerlo normalizado, sin variables sueltas y fácil de reconocer por Vosk, la clave quedará simplemente como 'secciones transversales'.

Como es una herramienta de utilidad del banco de trabajo Part, la vamos a agrupar en una carpeta de utilidades o simplemente con su nombre dentro de PartWorkbench.

Ubicación: tickets/DAV_Diccionario/PartWorkbench/cross_sections/

Archivo 1: cross_sections.py
Python

# Copyright (C) 2026 El Equipo del Proyecto DAV
# Universidad Autónoma de Entre Ríos (UADER)
# Bajo la dirección de Guillermo Gerard y Gallo Fabricio David
#
# Este programa es software libre: usted puede redistribuirlo y/o modificarlo
# bajo los términos de la Licencia Pública General GNU tal como fue publicada
# por la Fundación para el Software Libre, en la versión 3 de la Licencia.
#
# Este programa se distribuye con la esperanza de que sea útil,
# pero SIN NINGUNA GARANTÍA; incluso sin la garantía implícita de
# MERCANTIBILIDAD o APTITUD PARA UN PROPÓSITO PARTICULAR. Consulte la
# Licencia Pública General GNU para más detalles.
#
# Deberías haber recibido una copia de la Licencia Pública General GNU
# junto con este programa. Si no es así, consulte <http://www.gnu.org/licenses/>.

import FreeCADGui as Gui
from .ayuda import ayuda

cross_sections = {
    'secciones transversales': lambda: Gui.runCommand('Part_CrossSections', 0),
    'help': ayuda,
}

Archivo 2: ayuda.py
Python

# Copyright (C) 2026 El Equipo del Proyecto DAV
# Universidad Autónoma de Entre Ríos (UADER)
# Bajo la dirección de Guillermo Gerard y Gallo Fabricio David
#
# Este programa es software libre: usted puede redistribuirlo y/o modificarlo
# bajo los términos de la Licencia Pública General GNU tal como fue publicada
# por la Fundación para el Software Libre, en la versión 3 de la Licencia.
#
# Este programa se distribuye con la esperanza de que sea útil,
# pero SIN NINGUNA GARANTÍA; incluso sin la garantía implícita de
# MERCANTIBILIDAD o APTITUD PARA UN PROPÓSITO PARTICULAR. Consulte la
# Licencia Pública General GNU para más detalles.
#
# Deberías haber recibido una copia de la Licencia Pública General GNU
# junto con este programa. Si no es así, consulte <http://www.gnu.org/licenses/>.

def ayuda():
    print('Comandos disponibles en este nivel:')
    print('  secciones transversales - Crea múltiples secciones transversales a lo largo de un eje.')
    print('         Requiere: Tener un objeto base seleccionado en la vista 3D.')
    print('         Devuelve: Abre el panel de tareas para configurar el eje, cantidad y espaciado.')
    print('                   Al confirmar, genera un compuesto de perfiles (Cross sections).')
    print('         Nota: Herramienta de utilidad, muy usada para análisis de formas y diseño industrial.')

Ya quedó subsanado el script faltante y el comando listo para usarse. ¡Avisame cuál es el próximo ticket!
Concordia, Entre Ríos, Argentina

ticket part_loft

¡Recibido! Al analizar el ticket de Part_Loft, nos encontramos nuevamente con el problema del script nativo. El ticket sugiere instanciar el objeto directamente vía API (obj = doc.addObject("Part::Loft", "Loft")).  

Sin embargo, hacer un "Loft" (o desván) requiere seleccionar en un orden específico los perfiles (bocetos o alambres) que se van a unir. Si creamos el objeto vacío por API, el usuario de voz no tendrá cómo interactuar para cargarle los perfiles. La solución correcta aquí es invocar el panel interactivo de la herramienta en la interfaz gráfica usando Gui.runCommand('Part_Loft', 0).

En cuanto a las claves de voz sugeridas ("Hacer loft" y "Unir perfiles"), ambas son limpias, no tienen tildes y funcionan perfecto para Vosk, así que las incorporaremos tal cual en minúsculas.  

Como es una herramienta de modificación de formas, la ubicaremos en su propia carpeta dentro del PartWorkbench.

Ubicación sugerida: tickets/DAV_Diccionario/PartWorkbench/loft/

Archivo 1: loft.py
Python

# Copyright (C) 2026 El Equipo del Proyecto DAV
# Universidad Autónoma de Entre Ríos (UADER)
# Bajo la dirección de Guillermo Gerard y Gallo Fabricio David
#
# Este programa es software libre: usted puede redistribuirlo y/o modificarlo
# bajo los términos de la Licencia Pública General GNU tal como fue publicada
# por la Fundación para el Software Libre, en la versión 3 de la Licencia.
#
# Este programa se distribuye con la esperanza de que sea útil,
# pero SIN NINGUNA GARANTÍA; incluso sin la garantía implícita de
# MERCANTIBILIDAD o APTITUD PARA UN PROPÓSITO PARTICULAR. Consulte la
# Licencia Pública General GNU para más detalles.
#
# Deberías haber recibido una copia de la Licencia Pública General GNU
# junto con este programa. Si no es así, consulte <http://www.gnu.org/licenses/>.

import FreeCADGui as Gui
from .ayuda import ayuda


loft = {
    'hacer loft': lambda: Gui.runCommand('Part_Loft', 0),
    'unir perfiles': lambda: Gui.runCommand('Part_Loft', 0),
    'help': ayuda,
}

Archivo 2: ayuda.py
Python

# Copyright (C) 2026 El Equipo del Proyecto DAV
# Universidad Autónoma de Entre Ríos (UADER)
# Bajo la dirección de Guillermo Gerard y Gallo Fabricio David
#
# Este programa es software libre: usted puede redistribuirlo y/o modificarlo
# bajo los términos de la Licencia Pública General GNU tal como fue publicada
# por la Fundación para el Software Libre, en la versión 3 de la Licencia.
#
# Este programa se distribuye con la esperanza de que sea útil,
# pero SIN NINGUNA GARANTÍA; incluso sin la garantía implícita de
# MERCANTIBILIDAD o APTITUD PARA UN PROPÓSITO PARTICULAR. Consulte la
# Licencia Pública General GNU para más detalles.
#
# Deberías haber recibido una copia de la Licencia Pública General GNU
# junto con este programa. Si no es así, consulte <http://www.gnu.org/licenses/>.


def ayuda():
    print('Comandos disponibles en este nivel:')
    print('  hacer loft / unir perfiles - Crea una forma compleja uniendo varios perfiles transversales.')
    print('         Requiere: Tener al menos dos perfiles (Sketches o Wires) en el documento.')
    print('         Devuelve: Abre el panel de tareas para seleccionar perfiles. Genera un sólido o superficie Loft.')
    print('         Nota: Modificador avanzado. Ideal para formas orgánicas como cascos de barcos o conductos variables.')

El diccionario quedó listo y el error del script corregido. ¡Pasame el próximo ticket cuando gustes!
Concordia, Entre Ríos, Argentina

ticket part_mackeFace

¡Recibido el ticket de Part_MakeFace!

Al igual que en los tickets anteriores, vemos que el script sugerido (obj = doc.addObject("Part::Face", "Face"))  crea el objeto vacío por API en lugar de ejecutar la acción sobre la selección del usuario. Como esta función requiere que el usuario haya seleccionado previamente un alambre (wire) cerrado, lo correcto para el comando de voz es ejecutar la herramienta nativa de la interfaz que procesa esa selección: Gui.runCommand('Part_MakeFace', 0).  

La clave de voz sugerida incluye la variable "+ objeto", pero para mantener la compatibilidad estricta con Vosk y las expresiones limpias, la dejaremos simplemente como 'crear cara'.  

Ubicaremos esto en una nueva subcarpeta dentro del PartWorkbench.

Ubicación: tickets/DAV_Diccionario/PartWorkbench/make_face/

Archivo 1: make_face.py
Python

# Copyright (C) 2026 El Equipo del Proyecto DAV
# Universidad Autónoma de Entre Ríos (UADER)
# Bajo la dirección de Guillermo Gerard y Gallo Fabricio David
#
# Este programa es software libre: usted puede redistribuirlo y/o modificarlo
# bajo los términos de la Licencia Pública General GNU tal como fue publicada
# por la Fundación para el Software Libre, en la versión 3 de la Licencia.
#
# Este programa se distribuye con la esperanza de que sea útil,
# pero SIN NINGUNA GARANTÍA; incluso sin la garantía implícita de
# MERCANTIBILIDAD o APTITUD PARA UN PROPÓSITO PARTICULAR. Consulte la
# Licencia Pública General GNU para más detalles.
#
# Deberías haber recibido una copia de la Licencia Pública General GNU
# junto con este programa. Si no es así, consulte <http://www.gnu.org/licenses/>.

import FreeCADGui as Gui
from .ayuda import ayuda


make_face = {
    'crear cara': lambda: Gui.runCommand('Part_MakeFace', 0),
    'help': ayuda,
}

Archivo 2: ayuda.py
Python

# Copyright (C) 2026 El Equipo del Proyecto DAV
# Universidad Autónoma de Entre Ríos (UADER)
# Bajo la dirección de Guillermo Gerard y Gallo Fabricio David
#
# Este programa es software libre: usted puede redistribuirlo y/o modificarlo
# bajo los términos de la Licencia Pública General GNU tal como fue publicada
# por la Fundación para el Software Libre, en la versión 3 de la Licencia.
#
# Este programa se distribuye con la esperanza de que sea útil,
# pero SIN NINGUNA GARANTÍA; incluso sin la garantía implícita de
# MERCANTIBILIDAD o APTITUD PARA UN PROPÓSITO PARTICULAR. Consulte la
# Licencia Pública General GNU para más detalles.
#
# Deberías haber recibido una copia de la Licencia Pública General GNU
# junto con este programa. Si no es así, consulte <http://www.gnu.org/licenses/>.


def ayuda():
    print('Comandos disponibles en este nivel:')
    print('  crear cara - Crea una cara a partir de un conjunto de cables (wires) cerrados.')
    print('         Requiere: Tener seleccionado un wire cerrado en la vista 3D o en el árbol.')
    print('         Devuelve: Una superficie (Face).')
    print('         Nota: Es una función muy útil para convertir dibujos de Draft en superficies planas.')

El diccionario está listo. Pasame el próximo ticket de tu lista para continuar.
Concordia, Entre Ríos, Argentina

ticket part_offset

¡Recibido el ticket de Part_Offset!

Al igual que en los casos de Loft y MakeFace, el script proporcionado en el ticket instancia el objeto directamente por API (obj = doc.addObject("Part::Offset", "Offset")). Como esta herramienta actúa como un modificador que requiere un "Objeto base" ya existente en el documento para funcionar, crear el objeto Offset vacío por código no es la mejor opción. Lo correcto para que el usuario de voz pueda interactuar naturalmente es invocar el comando de la interfaz gráfica: Gui.runCommand('Part_Offset', 0).  

Las palabras clave sugeridas son "Desfase" u "Offset" más la distancia. Para mantener la normalización exigida por Vosk (minúsculas, sin variables complejas adheridas de forma estricta), usaremos 'desfase' y 'offset'.  

Ubicaremos este comando en su propia subcarpeta dentro del PartWorkbench.

Ubicación: tickets/DAV_Diccionario/PartWorkbench/offset/

Archivo 1: offset.py
Python

# Copyright (C) 2026 El Equipo del Proyecto DAV
# Universidad Autónoma de Entre Ríos (UADER)
# Bajo la dirección de Guillermo Gerard y Gallo Fabricio David
#
# Este programa es software libre: usted puede redistribuirlo y/o modificarlo
# bajo los términos de la Licencia Pública General GNU tal como fue publicada
# por la Fundación para el Software Libre, en la versión 3 de la Licencia.
#
# Este programa se distribuye con la esperanza de que sea útil,
# pero SIN NINGUNA GARANTÍA; incluso sin la garantía implícita de
# MERCANTIBILIDAD o APTITUD PARA UN PROPÓSITO PARTICULAR. Consulte la
# Licencia Pública General GNU para más detalles.
#
# Deberías haber recibido una copia de la Licencia Pública General GNU
# junto con este programa. Si no es así, consulte <http://www.gnu.org/licenses/>.

import FreeCADGui as Gui
from .ayuda import ayuda


offset = {
    'desfase': lambda: Gui.runCommand('Part_Offset', 0),
    'offset': lambda: Gui.runCommand('Part_Offset', 0),
    'help': ayuda,
}

Archivo 2: ayuda.py
Python

# Copyright (C) 2026 El Equipo del Proyecto DAV
# Universidad Autónoma de Entre Ríos (UADER)
# Bajo la dirección de Guillermo Gerard y Gallo Fabricio David
#
# Este programa es software libre: usted puede redistribuirlo y/o modificarlo
# bajo los términos de la Licencia Pública General GNU tal como fue publicada
# por la Fundación para el Software Libre, en la versión 3 de la Licencia.
#
# Este programa se distribuye con la esperanza de que sea útil,
# pero SIN NINGUNA GARANTÍA; incluso sin la garantía implícita de
# MERCANTIBILIDAD o APTITUD PARA UN PROPÓSITO PARTICULAR. Consulte la
# Licencia Pública General GNU para más detalles.
#
# Deberías haber recibido una copia de la Licencia Pública General GNU
# junto con este programa. Si no es así, consulte <http://www.gnu.org/licenses/>.


def ayuda():
    print('Comandos disponibles en este nivel:')
    print('  desfase / offset - Crea una copia de una forma desplazada a una distancia constante.')
    print('         Requiere: Tener un objeto base seleccionado.')
    print('         Devuelve: Abre el panel de tareas para configurar la distancia de desfase (float).')
    print('         Nota: Es un modificador que puede usarse para ensanchar o encoger sólidos.')

El diccionario quedó configurado. Pasame el próximo ticket de tu lista.
Concordia, Entre Ríos, Argentina

ticket part_offset2D

¡Recibido el ticket de Part_Offset2D!   

Nuevamente nos encontramos con el mismo patrón que en los modificadores anteriores: el ticket sugiere instanciar el objeto vacío por API (obj = doc.addObject("Part::Offset2D", "Offset2D")). Dado que esta es una herramienta interactiva que requiere que el usuario haya seleccionado previamente un perfil 2D (como un boceto o un wire) para luego configurar la distancia, la forma correcta de implementarlo para el uso por voz es invocar el panel de tareas de la interfaz gráfica usando Gui.runCommand('Part_Offset2D', 0).  

Las palabras clave sugeridas son "Contorno" o "Borde". Al normalizarlas para Vosk, quitamos la variable de la distancia y las dejamos simplemente como 'contorno' y 'borde'.  

Vamos a agrupar este comando en su propia subcarpeta dentro del PartWorkbench.

Ubicación: tickets/DAV_Diccionario/PartWorkbench/offset2d/

Archivo 1: offset2d.py
Python

# Copyright (C) 2026 El Equipo del Proyecto DAV
# Universidad Autónoma de Entre Ríos (UADER)
# Bajo la dirección de Guillermo Gerard y Gallo Fabricio David
#
# Este programa es software libre: usted puede redistribuirlo y/o modificarlo
# bajo los términos de la Licencia Pública General GNU tal como fue publicada
# por la Fundación para el Software Libre, en la versión 3 de la Licencia.
#
# Este programa se distribuye con la esperanza de que sea útil,
# pero SIN NINGUNA GARANTÍA; incluso sin la garantía implícita de
# MERCANTIBILIDAD o APTITUD PARA UN PROPÓSITO PARTICULAR. Consulte la
# Licencia Pública General GNU para más detalles.
#
# Deberías haber recibido una copia de la Licencia Pública General GNU
# junto con este programa. Si no es así, consulte <http://www.gnu.org/licenses/>.

import FreeCADGui as Gui
from .ayuda import ayuda


offset2d = {
    'contorno': lambda: Gui.runCommand('Part_Offset2D', 0),
    'borde': lambda: Gui.runCommand('Part_Offset2D', 0),
    'help': ayuda,
}

Archivo 2: ayuda.py
Python

# Copyright (C) 2026 El Equipo del Proyecto DAV
# Universidad Autónoma de Entre Ríos (UADER)
# Bajo la dirección de Guillermo Gerard y Gallo Fabricio David
#
# Este programa es software libre: usted puede redistribuirlo y/o modificarlo
# bajo los términos de la Licencia Pública General GNU tal como fue publicada
# por la Fundación para el Software Libre, en la versión 3 de la Licencia.
#
# Este programa se distribuye con la esperanza de que sea útil,
# pero SIN NINGUNA GARANTÍA; incluso sin la garantía implícita de
# MERCANTIBILIDAD o APTITUD PARA UN PROPÓSITO PARTICULAR. Consulte la
# Licencia Pública General GNU para más detalles.
#
# Deberías haber recibido una copia de la Licencia Pública General GNU
# junto con este programa. Si no es así, consulte <http://www.gnu.org/licenses/>.


def ayuda():
    print('Comandos disponibles en este nivel:')
    print('  contorno / borde - Desplaza el perfil de una forma 2D a una distancia específica.')
    print('         Requiere: Tener seleccionado un perfil 2D (cables/wires o bocetos/sketches).')
    print('         Devuelve: Abre el panel de tareas para configurar la distancia. Genera un perfil desplazado.')
    print('         Nota: Es un modificador 2D, específico para formas bidimensionales.')

El diccionario 2D ya está integrado. ¡Pasame el próximo ticket cuando quieras!
Concordia, Entre Ríos, Argentina

ticke projectionOnSurface

¡Recibido el ticket de Part_ProjectionOnSurface!

Nuevamente nos encontramos con el campo del script nativo incompleto, ya que el ticket solo trae un comentario (# Proyecta una forma sobre una cara) en lugar del código ejecutable. Dado que esta operación requiere que el usuario haya seleccionado primero el perfil 2D y la superficie de destino, lo correcto y funcional para el comando por voz es abrir la herramienta interactiva usando Gui.runCommand('Part_ProjectionOnSurface', 0).

Para las palabras clave, el ticket sugiere "Proyectar dibujo sobre superficie". Adaptando esto a las reglas de Vosk (minúsculas, sin caracteres especiales y fácil de pronunciar de corrido), usaremos 'proyectar dibujo' y 'proyectar sobre superficie'.

Agruparemos este comando en su propia subcarpeta dentro del PartWorkbench.

Ubicación: tickets/DAV_Diccionario/PartWorkbench/projection_on_surface/

Archivo 1: projection_on_surface.py
Python

# Copyright (C) 2026 El Equipo del Proyecto DAV
# Universidad Autónoma de Entre Ríos (UADER)
# Bajo la dirección de Guillermo Gerard y Gallo Fabricio David
#
# Este programa es software libre: usted puede redistribuirlo y/o modificarlo
# bajo los términos de la Licencia Pública General GNU tal como fue publicada
# por la Fundación para el Software Libre, en la versión 3 de la Licencia.
#
# Este programa se distribuye con la esperanza de que sea útil,
# pero SIN NINGUNA GARANTÍA; incluso sin la garantía implícita de
# MERCANTIBILIDAD o APTITUD PARA UN PROPÓSITO PARTICULAR. Consulte la
# Licencia Pública General GNU para más detalles.
#
# Deberías haber recibido una copia de la Licencia Pública General GNU
# junto con este programa. Si no es así, consulte <http://www.gnu.org/licenses/>.

import FreeCADGui as Gui
from .ayuda import ayuda


projection_on_surface = {
    'proyectar dibujo': lambda: Gui.runCommand('Part_ProjectionOnSurface', 0),
    'proyectar sobre superficie': lambda: Gui.runCommand('Part_ProjectionOnSurface', 0),
    'help': ayuda,
}

Archivo 2: ayuda.py
Python

# Copyright (C) 2026 El Equipo del Proyecto DAV
# Universidad Autónoma de Entre Ríos (UADER)
# Bajo la dirección de Guillermo Gerard y Gallo Fabricio David
#
# Este programa es software libre: usted puede redistribuirlo y/o modificarlo
# bajo los términos de la Licencia Pública General GNU tal como fue publicada
# por la Fundación para el Software Libre, en la versión 3 de la Licencia.
#
# Este programa se distribuye con la esperanza de que sea útil,
# pero SIN NINGUNA GARANTÍA; incluso sin la garantía implícita de
# MERCANTIBILIDAD o APTITUD PARA UN PROPÓSITO PARTICULAR. Consulte la
# Licencia Pública General GNU para más detalles.
#
# Deberías haber recibido una copia de la Licencia Pública General GNU
# junto con este programa. Si no es así, consulte <http://www.gnu.org/licenses/>.


def ayuda():
    print('Comandos disponibles en este nivel:')
    print('  proyectar dibujo / proyectar sobre superficie - Proyecta un dibujo o perfil sobre la superficie de un sólido.')
    print('         Requiere: Tener seleccionado un perfil 2D y una superficie de destino.')
    print('         Devuelve: Abre la herramienta para generar las curvas proyectadas.')
    print('         Nota: La proyección sigue la curvatura de la superficie de destino.')

El diccionario de proyección quedó configurado y solucionamos el faltante del script. ¡Espero el próximo ticket de la lista para continuar!

ticket part_revolve

¡Recibido el ticket de Part_Revolve!

Una vez más, el ticket presenta el patrón de instanciar el objeto directamente por la API (obj = doc.addObject("Part::Revolution", "Revolve")). Dado que la revolución es un modificador que necesita una forma base, un eje de rotación y un ángulo, crear el objeto vacío ocultaría estas opciones al usuario de voz. La forma correcta para integrarlo y permitir la interacción con el panel de tareas es invocar el comando nativo de la interfaz gráfica: Gui.runCommand('Part_Revolve', 0).  

Para la clave de voz, el ticket sugiere "Revolución" + objeto + ángulo. Aplicando la normalización estricta para Vosk (minúsculas, sin tildes y eliminando las variables dinámicas para evitar errores de reconocimiento), la clave quedará en 'revolucion'.  

Vamos a crear su subcarpeta correspondiente dentro del PartWorkbench.

Ubicación: tickets/DAV_Diccionario/PartWorkbench/revolve/

Archivo 1: revolve.py
Python

# Copyright (C) 2026 El Equipo del Proyecto DAV
# Universidad Autónoma de Entre Ríos (UADER)
# Bajo la dirección de Guillermo Gerard y Gallo Fabricio David
#
# Este programa es software libre: usted puede redistribuirlo y/o modificarlo
# bajo los términos de la Licencia Pública General GNU tal como fue publicada
# por la Fundación para el Software Libre, en la versión 3 de la Licencia.
#
# Este programa se distribuye con la esperanza de que sea útil,
# pero SIN NINGUNA GARANTÍA; incluso sin la garantía implícita de
# MERCANTIBILIDAD o APTITUD PARA UN PROPÓSITO PARTICULAR. Consulte la
# Licencia Pública General GNU para más detalles.
#
# Deberías haber recibido una copia de la Licencia Pública General GNU
# junto con este programa. Si no es así, consulte <http://www.gnu.org/licenses/>.

import FreeCADGui as Gui
from .ayuda import ayuda


revolve = {
    'revolucion': lambda: Gui.runCommand('Part_Revolve', 0),
    'help': ayuda,
}

Archivo 2: ayuda.py
Python

# Copyright (C) 2026 El Equipo del Proyecto DAV
# Universidad Autónoma de Entre Ríos (UADER)
# Bajo la dirección de Guillermo Gerard y Gallo Fabricio David
#
# Este programa es software libre: usted puede redistribuirlo y/o modificarlo
# bajo los términos de la Licencia Pública General GNU tal como fue publicada
# por la Fundación para el Software Libre, en la versión 3 de la Licencia.
#
# Este programa se distribuye con la esperanza de que sea útil,
# pero SIN NINGUNA GARANTÍA; incluso sin la garantía implícita de
# MERCANTIBILIDAD o APTITUD PARA UN PROPÓSITO PARTICULAR. Consulte la
# Licencia Pública General GNU para más detalles.
#
# Deberías haber recibido una copia de la Licencia Pública General GNU
# junto con este programa. Si no es así, consulte <http://www.gnu.org/licenses/>.


def ayuda():
    print('Comandos disponibles en este nivel:')
    print('  revolucion - Gira una forma alrededor de un eje para crear un sólido simétrico.')
    print('         Requiere: Tener seleccionada una forma base.')
    print('         Devuelve: Abre el panel de tareas para configurar el eje de rotación (Vector) y el ángulo (float).')
    print('         Nota: Es un modificador útil para crear piezas cilíndricas o circulares complejas.')

El diccionario de revolución ya está integrado y con el script ajustado para interactuar correctamente. ¡Pasame el próximo de la lista!

ticket ruledSurface

¡Recibido el ticket de Part_RuledSurface!   

Una vez más, vemos que el script nativo sugerido en el ticket crea el objeto de la superficie directamente mediante la API (obj = doc.addObject("Part::RuledSurface", "RuledSurface")). Sin embargo, la descripción aclara que esta herramienta requiere que el usuario haya seleccionado previamente dos curvas o aristas independientes. Para que el usuario de voz pueda hacer las selecciones en la interfaz y luego ejecutar la acción, la forma correcta de implementarlo es invocando el comando de la interfaz gráfica: Gui.runCommand('Part_RuledSurface', 0).  

Las palabras sugeridas para los comandos por voz son "Unir curvas" o "Superficie reglada". Las vamos a pasar a minúsculas para mantener la compatibilidad con el motor Vosk, quedando como 'unir curvas' y 'superficie reglada'.  

Vamos a crear la subcarpeta correspondiente dentro del PartWorkbench.

Ubicación: tickets/DAV_Diccionario/PartWorkbench/ruled_surface/

Archivo 1: ruled_surface.py
Python

# Copyright (C) 2026 El Equipo del Proyecto DAV
# Universidad Autónoma de Entre Ríos (UADER)
# Bajo la dirección de Guillermo Gerard y Gallo Fabricio David
#
# Este programa es software libre: usted puede redistribuirlo y/o modificarlo
# bajo los términos de la Licencia Pública General GNU tal como fue publicada
# por la Fundación para el Software Libre, en la versión 3 de la Licencia.
#
# Este programa se distribuye con la esperanza de que sea útil,
# pero SIN NINGUNA GARANTÍA; incluso sin la garantía implícita de
# MERCANTIBILIDAD o APTITUD PARA UN PROPÓSITO PARTICULAR. Consulte la
# Licencia Pública General GNU para más detalles.
#
# Deberías haber recibido una copia de la Licencia Pública General GNU
# junto con este programa. Si no es así, consulte <http://www.gnu.org/licenses/>.

import FreeCADGui as Gui
from .ayuda import ayuda


ruled_surface = {
    'unir curvas': lambda: Gui.runCommand('Part_RuledSurface', 0),
    'superficie reglada': lambda: Gui.runCommand('Part_RuledSurface', 0),
    'help': ayuda,
}

Archivo 2: ayuda.py
Python

# Copyright (C) 2026 El Equipo del Proyecto DAV
# Universidad Autónoma de Entre Ríos (UADER)
# Bajo la dirección de Guillermo Gerard y Gallo Fabricio David
#
# Este programa es software libre: usted puede redistribuirlo y/o modificarlo
# bajo los términos de la Licencia Pública General GNU tal como fue publicada
# por la Fundación para el Software Libre, en la versión 3 de la Licencia.
#
# Este programa se distribuye con la esperanza de que sea útil,
# pero SIN NINGUNA GARANTÍA; incluso sin la garantía implícita de
# MERCANTIBILIDAD o APTITUD PARA UN PROPÓSITO PARTICULAR. Consulte la
# Licencia Pública General GNU para más detalles.
#
# Deberías haber recibido una copia de la Licencia Pública General GNU
# junto con este programa. Si no es así, consulte <http://www.gnu.org/licenses/>.


def ayuda():
    print('Comandos disponibles en este nivel:')
    print('  unir curvas / superficie reglada - Crea una superficie reglada entre dos curvas seleccionadas.')
    print('         Requiere: Tener seleccionadas exactamente dos curvas/aristas independientes.')
    print('         Devuelve: Una superficie reglada (Ruled Surface).')
    print('         Nota: Las curvas deben tener una orientación similar para evitar torsiones.')

El comando para la superficie reglada ya quedó corregido y documentado con la advertencia sobre la orientación de las curvas para evitar torsiones. ¡Pasame el próximo ticket de la lista para continuar con el trabajo!  

ticket scale

¡Recibido el ticket de Part_Scale!

Nuevamente nos topamos con el mismo patrón: el ticket sugiere instanciar el objeto escalado directamente vía API (obj = doc.addObject("Part::Scaled", "Scale")). Como esta herramienta de transformación requiere que el usuario seleccione un objeto base y luego introduzca un factor de escala (que puede ser uniforme o distinto en cada eje X, Y, Z), la mejor manera de implementarlo para comandos de voz es abriendo el panel de tareas en la interfaz. Por lo tanto, usaremos el comando nativo Gui.runCommand('Part_Scale', 0).  

Las palabras sugeridas son "Escalar" o "Agrandar" seguido del objeto y el factor. Limpiando estas frases para que Vosk las reconozca sin problemas y sin variables complejas, usaremos las claves 'escalar' y 'agrandar'.  

Armaremos la subcarpeta correspondiente dentro del PartWorkbench.

Ubicación: tickets/DAV_Diccionario/PartWorkbench/scale/

Archivo 1: scale.py
Python

# Copyright (C) 2026 El Equipo del Proyecto DAV
# Universidad Autónoma de Entre Ríos (UADER)
# Bajo la dirección de Guillermo Gerard y Gallo Fabricio David
#
# Este programa es software libre: usted puede redistribuirlo y/o modificarlo
# bajo los términos de la Licencia Pública General GNU tal como fue publicada
# por la Fundación para el Software Libre, en la versión 3 de la Licencia.
#
# Este programa se distribuye con la esperanza de que sea útil,
# pero SIN NINGUNA GARANTÍA; incluso sin la garantía implícita de
# MERCANTIBILIDAD o APTITUD PARA UN PROPÓSITO PARTICULAR. Consulte la
# Licencia Pública General GNU para más detalles.
#
# Deberías haber recibido una copia de la Licencia Pública General GNU
# junto con este programa. Si no es así, consulte <http://www.gnu.org/licenses/>.

import FreeCADGui as Gui
from .ayuda import ayuda


scale = {
    'escalar': lambda: Gui.runCommand('Part_Scale', 0),
    'agrandar': lambda: Gui.runCommand('Part_Scale', 0),
    'help': ayuda,
}

Archivo 2: ayuda.py
Python

# Copyright (C) 2026 El Equipo del Proyecto DAV
# Universidad Autónoma de Entre Ríos (UADER)
# Bajo la dirección de Guillermo Gerard y Gallo Fabricio David
#
# Este programa es software libre: usted puede redistribuirlo y/o modificarlo
# bajo los términos de la Licencia Pública General GNU tal como fue publicada
# por la Fundación para el Software Libre, en la versión 3 de la Licencia.
#
# Este programa se distribuye con la esperanza de que sea útil,
# pero SIN NINGUNA GARANTÍA; incluso sin la garantía implícita de
# MERCANTIBILIDAD o APTITUD PARA UN PROPÓSITO PARTICULAR. Consulte la
# Licencia Pública General GNU para más detalles.
#
# Deberías haber recibido una copia de la Licencia Pública General GNU
# junto con este programa. Si no es así, consulte <http://www.gnu.org/licenses/>.


def ayuda():
    print('Comandos disponibles en este nivel:')
    print('  escalar / agrandar - Cambia el tamaño de una forma mediante un factor de escala.')
    print('         Requiere: Tener seleccionado un objeto base.')
    print('         Devuelve: Abre el panel de tareas para configurar el factor de escala (Vector/Float).')
    print('         Nota: Puede escalar de forma uniforme o distinta en cada eje (X, Y, Z).')

El diccionario de escala ya quedó corregido e integrado. ¡Pasame el próximo ticket de la lista para seguir avanzando!

 ticket section

¡Recibido el ticket de Part_Section!

Al igual que en los tickets anteriores de modificadores e intersecciones, el script provisto (obj = doc.addObject("Part::Section", "Section")) crea el objeto por API, pero esta herramienta necesita que el usuario tenga seleccionados dos objetos que se crucen en la interfaz. Para respetar el flujo de trabajo del usuario mediante voz, la forma correcta es invocar el comando interactivo: Gui.runCommand('Part_Section', 0).  

Las palabras sugeridas son "Obtener sección" o "Intersección". Normalizándolas para Vosk sin tildes ni mayúsculas, nos quedan las claves 'obtener seccion' e 'interseccion'.  

Armaremos la subcarpeta correspondiente dentro del PartWorkbench.

Ubicación: tickets/DAV_Diccionario/PartWorkbench/section/

Archivo 1: section.py
Python

# Copyright (C) 2026 El Equipo del Proyecto DAV
# Universidad Autónoma de Entre Ríos (UADER)
# Bajo la dirección de Guillermo Gerard y Gallo Fabricio David
#
# Este programa es software libre: usted puede redistribuirlo y/o modificarlo
# bajo los términos de la Licencia Pública General GNU tal como fue publicada
# por la Fundación para el Software Libre, en la versión 3 de la Licencia.
#
# Este programa se distribuye con la esperanza de que sea útil,
# pero SIN NINGUNA GARANTÍA; incluso sin la garantía implícita de
# MERCANTIBILIDAD o APTITUD PARA UN PROPÓSITO PARTICULAR. Consulte la
# Licencia Pública General GNU para más detalles.
#
# Deberías haber recibido una copia de la Licencia Pública General GNU
# junto con este programa. Si no es así, consulte <http://www.gnu.org/licenses/>.

import FreeCADGui as Gui
from .ayuda import ayuda


section = {
    'obtener seccion': lambda: Gui.runCommand('Part_Section', 0),
    'interseccion': lambda: Gui.runCommand('Part_Section', 0),
    'help': ayuda,
}

Archivo 2: ayuda.py
Python

# Copyright (C) 2026 El Equipo del Proyecto DAV
# Universidad Autónoma de Entre Ríos (UADER)
# Bajo la dirección de Guillermo Gerard y Gallo Fabricio David
#
# Este programa es software libre: usted puede redistribuirlo y/o modificarlo
# bajo los términos de la Licencia Pública General GNU tal como fue publicada
# por la Fundación para el Software Libre, en la versión 3 de la Licencia.
#
# Este programa se distribuye con la esperanza de que sea útil,
# pero SIN NINGUNA GARANTÍA; incluso sin la garantía implícita de
# MERCANTIBILIDAD o APTITUD PARA UN PROPÓSITO PARTICULAR. Consulte la
# Licencia Pública General GNU para más detalles.
#
# Deberías haber recibido una copia de la Licencia Pública General GNU
# junto con este programa. Si no es así, consulte <http://www.gnu.org/licenses/>.


def ayuda():
    print('Comandos disponibles en este nivel:')
    print('  obtener seccion / interseccion - Genera la intersección entre dos objetos como una línea o curva.')
    print('         Requiere: Tener seleccionados dos objetos que se crucen en la vista 3D.')
    print('         Devuelve: Curvas de sección.')
    print('         Nota: No crea un sólido, sino el perfil donde se tocan los objetos.')

El comando de sección quedó resuelto y documentado. ¡Pasame el siguiente ticket!
Concordia, Entre Ríos, Argentina

ticket sweep

¡Recibido el ticket de Part_Sweep!

Volvemos a encontrar el mismo detalle con el script nativo. El ticket sugiere la instanciación directa vía API (obj = doc.addObject("Part::Sweep", "Sweep")). Al tratarse de un modificador avanzado que exige elegir un perfil y una trayectoria, si creamos el objeto vacío, el usuario de voz no tendría forma de asignar esas geometrías. La solución adecuada para interactuar con el panel de tareas es invocar el comando interactivo de la interfaz gráfica: Gui.runCommand('Part_Sweep', 0).  

En cuanto a las palabras clave, el ticket propone "Barrer perfil" + trayectoria. Para ajustarnos a las reglas de normalización de Vosk y tener comandos directos sin variables dinámicas engorrosas, utilizaremos 'barrer perfil' y agregaremos 'barrido' como alternativa corta.  

Crearemos la subcarpeta correspondiente dentro del PartWorkbench.

Ubicación: tickets/DAV_Diccionario/PartWorkbench/sweep/

Archivo 1: sweep.py
Python

# Copyright (C) 2026 El Equipo del Proyecto DAV
# Universidad Autónoma de Entre Ríos (UADER)
# Bajo la dirección de Guillermo Gerard y Gallo Fabricio David
#
# Este programa es software libre: usted puede redistribuirlo y/o modificarlo
# bajo los términos de la Licencia Pública General GNU tal como fue publicada
# por la Fundación para el Software Libre, en la versión 3 de la Licencia.
#
# Este programa se distribuye con la esperanza de que sea útil,
# pero SIN NINGUNA GARANTÍA; incluso sin la garantía implícita de
# MERCANTIBILIDAD o APTITUD PARA UN PROPÓSITO PARTICULAR. Consulte la
# Licencia Pública General GNU para más detalles.
#
# Deberías haber recibido una copia de la Licencia Pública General GNU
# junto con este programa. Si no es así, consulte <http://www.gnu.org/licenses/>.

import FreeCADGui as Gui
from .ayuda import ayuda


sweep = {
    'barrer perfil': lambda: Gui.runCommand('Part_Sweep', 0),
    'barrido': lambda: Gui.runCommand('Part_Sweep', 0),
    'help': ayuda,
}

Archivo 2: ayuda.py
Python

# Copyright (C) 2026 El Equipo del Proyecto DAV
# Universidad Autónoma de Entre Ríos (UADER)
# Bajo la dirección de Guillermo Gerard y Gallo Fabricio David
#
# Este programa es software libre: usted puede redistribuirlo y/o modificarlo
# bajo los términos de la Licencia Pública General GNU tal como fue publicada
# por la Fundación para el Software Libre, en la versión 3 de la Licencia.
#
# Este programa se distribuye con la esperanza de que sea útil,
# pero SIN NINGUNA GARANTÍA; incluso sin la garantía implícita de
# MERCANTIBILIDAD o APTITUD PARA UN PROPÓSITO PARTICULAR. Consulte la
# Licencia Pública General GNU para más detalles.
#
# Deberías haber recibido una copia de la Licencia Pública General GNU
# junto con este programa. Si no es así, consulte <http://www.gnu.org/licenses/>.


def ayuda():
    print('Comandos disponibles en este nivel:')
    print('  barrer perfil / barrido - Desplaza un perfil a lo largo de una trayectoria definida.')
    print('         Requiere: Tener seleccionado o definir un perfil (sección) y una trayectoria (path).')
    print('         Devuelve: Abre el panel de tareas para configurar la operación. Genera un sólido o superficie de barrido.')
    print('         Nota: La trayectoria puede ser una línea, arco o curva compleja.')

El diccionario de barrido quedó corregido e integrado perfectamente al esquema. ¡Pasame el próximo ticket de la lista para continuar!

ticket thickness

¡Recibido el ticket de Part_Thickness!

Una vez más, el ticket muestra la creación del objeto vacío mediante la API (obj = doc.addObject("Part::Thickness", "Thickness")). Como esta herramienta convierte un sólido en una carcasa hueca y requiere que el usuario haya seleccionado un sólido base y las caras a eliminar, instanciar el objeto por código no le permitiría al usuario interactuar correctamente con el panel de la herramienta. La forma correcta para integrarlo a los comandos de voz es mediante la interfaz gráfica: Gui.runCommand('Part_Thickness', 0).  

Las palabras sugeridas son "Dar espesor" o "Hacer hueco" más la medida. Para cumplir con las exigencias del motor Vosk (comandos en minúsculas, sin tildes y sin variables sueltas), las claves quedarán definidas como 'dar espesor' y 'hacer hueco'.  

A continuación, la estructura para este modificador en su propia subcarpeta dentro del PartWorkbench.

Ubicación: tickets/DAV_Diccionario/PartWorkbench/thickness/

Archivo 1: thickness.py
Python

# Copyright (C) 2026 El Equipo del Proyecto DAV
# Universidad Autónoma de Entre Ríos (UADER)
# Bajo la dirección de Guillermo Gerard y Gallo Fabricio David
#
# Este programa es software libre: usted puede redistribuirlo y/o modificarlo
# bajo los términos de la Licencia Pública General GNU tal como fue publicada
# por la Fundación para el Software Libre, en la versión 3 de la Licencia.
#
# Este programa se distribuye con la esperanza de que sea útil,
# pero SIN NINGUNA GARANTÍA; incluso sin la garantía implícita de
# MERCANTIBILIDAD o APTITUD PARA UN PROPÓSITO PARTICULAR. Consulte la
# Licencia Pública General GNU para más detalles.
#
# Deberías haber recibido una copia de la Licencia Pública General GNU
# junto con este programa. Si no es así, consulte <http://www.gnu.org/licenses/>.

import FreeCADGui as Gui
from .ayuda import ayuda


thickness = {
    'dar espesor': lambda: Gui.runCommand('Part_Thickness', 0),
    'hacer hueco': lambda: Gui.runCommand('Part_Thickness', 0),
    'help': ayuda,
}

Archivo 2: ayuda.py
Python

# Copyright (C) 2026 El Equipo del Proyecto DAV
# Universidad Autónoma de Entre Ríos (UADER)
# Bajo la dirección de Guillermo Gerard y Gallo Fabricio David
#
# Este programa es software libre: usted puede redistribuirlo y/o modificarlo
# bajo los términos de la Licencia Pública General GNU tal como fue publicada
# por la Fundación para el Software Libre, en la versión 3 de la Licencia.
#
# Este programa se distribuye con la esperanza de que sea útil,
# pero SIN NINGUNA GARANTÍA; incluso sin la garantía implícita de
# MERCANTIBILIDAD o APTITUD PARA UN PROPÓSITO PARTICULAR. Consulte la
# Licencia Pública General GNU para más detalles.
#
# Deberías haber recibido una copia de la Licencia Pública General GNU
# junto con este programa. Si no es así, consulte <http://www.gnu.org/licenses/>.


def ayuda():
    print('Comandos disponibles en este nivel:')
    print('  dar espesor / hacer hueco - Convierte un sólido en una carcasa hueca con un grosor definido.')
    print('         Requiere: Tener seleccionado un sólido base y las caras a eliminar.')
    print('         Devuelve: Abre el panel de tareas para configurar el espesor (float). Genera un objeto vaciado (Shell).')
    print('         Nota: Es un modificador ideal para crear cajas, carcasas o recipientes.')

El comando de espesor/vaciado ya está corregido y listo. ¡Pasame el próximo ticket de la lista!

ticket partdesing-preferences

¡Recibido el ticket de PartDesign Preferences!

Acá nos encontramos con que el ticket indica la ruta de la interfaz gráfica (Edit → Preferences → Part/Part Design)  en lugar de un comando nativo de la API. En FreeCAD, el comando global para abrir la ventana de preferencias es Std_DlgPreferences. Si bien esto abrirá la ventana general, es el punto de entrada correcto, y el usuario podrá interactuar con las pestañas de Part/PartDesign.  

Para las palabras clave, el ticket sugiere varias opciones. Para mantener la consistencia con las reglas de Vosk (minúsculas y sin caracteres especiales), utilizaremos 'preferencias de part', 'configuracion partdesign', 'shape appearance' y 'shape view'.  

Vamos a agrupar esto en una subcarpeta dedicada a preferencias dentro del PartWorkbench.

Ubicación: tickets/DAV_Diccionario/PartWorkbench/preferences/

Archivo 1: preferences.py
Python

# Copyright (C) 2026 El Equipo del Proyecto DAV
# Universidad Autónoma de Entre Ríos (UADER)
# Bajo la dirección de Guillermo Gerard y Gallo Fabricio David
#
# Este programa es software libre: usted puede redistribuirlo y/o modificarlo
# bajo los términos de la Licencia Pública General GNU tal como fue publicada
# por la Fundación para el Software Libre, en la versión 3 de la Licencia.
#
# Este programa se distribuye con la esperanza de que sea útil,
# pero SIN NINGUNA GARANTÍA; incluso sin la garantía implícita de
# MERCANTIBILIDAD o APTITUD PARA UN PROPÓSITO PARTICULAR. Consulte la
# Licencia Pública General GNU para más detalles.
#
# Deberías haber recibido una copia de la Licencia Pública General GNU
# junto con este programa. Si no es así, consulte <http://www.gnu.org/licenses/>.

import FreeCADGui as Gui
from .ayuda import ayuda


preferences = {
    'preferencias de part': lambda: Gui.runCommand('Std_DlgPreferences', 0),
    'configuracion partdesign': lambda: Gui.runCommand('Std_DlgPreferences', 0),
    'shape appearance': lambda: Gui.runCommand('Std_DlgPreferences', 0),
    'shape view': lambda: Gui.runCommand('Std_DlgPreferences', 0),
    'help': ayuda,
}

Archivo 2: ayuda.py
Python

# Copyright (C) 2026 El Equipo del Proyecto DAV
# Universidad Autónoma de Entre Ríos (UADER)
# Bajo la dirección de Guillermo Gerard y Gallo Fabricio David
#
# Este programa es software libre: usted puede redistribuirlo y/o modificarlo
# bajo los términos de la Licencia Pública General GNU tal como fue publicada
# por la Fundación para el Software Libre, en la versión 3 de la Licencia.
#
# Este programa se distribuye con la esperanza de que sea útil,
# pero SIN NINGUNA GARANTÍA; incluso sin la garantía implícita de
# MERCANTIBILIDAD o APTITUD PARA UN PROPÓSITO PARTICULAR. Consulte la
# Licencia Pública General GNU para más detalles.
#
# Deberías haber recibido una copia de la Licencia Pública General GNU
# junto con este programa. Si no es así, consulte <http://www.gnu.org/licenses/>.


def ayuda():
    print('Comandos disponibles en este nivel:')
    print('  preferencias de part / configuracion partdesign - Abre la ventana de preferencias.')
    print('         Requiere: Tener cargado el Part Workbench o el PartDesign Workbench en la sesión actual[cite: 67].')
    print('         Devuelve: Una ventana de configuración con opciones para modificar el comportamiento[cite: 68].')
    print('         Nota: Permite configurar operaciones booleanas automáticas, refinamiento y apariencia de objetos 3D.')
    print('               También permite ajustar parámetros avanzados de tessellation mediante el Parameter Editor[cite: 70].')

El diccionario de preferencias de Part/PartDesign quedó integrado. Para probarlo sin problemas en Ubuntu, recordá que podés importar preferences directo en la consola de FreeCAD y ejecutar los lambdas.

¡Pasame el próximo ticket de la lista para continuar!

ticket finetuning-preferences

¡Recibido el ticket de Fine Tuning!

Aunque se trata de una configuración global del sistema y no exclusiva de una herramienta de modelado geométrico, el comando nativo subyacente para abrir "Tools → Edit parameters" en FreeCAD es Std_DlgParameter. Es fundamental usar este comando para que la ventana se abra correctamente en la interfaz gráfica.  

Para las palabras clave, el ticket sugiere varias opciones en inglés y español. Adaptándolas a las reglas de normalización de Vosk (todo en minúsculas, sin tildes ni caracteres especiales), utilizaremos 'fine tuning', 'configuracion avanzada' y 'modificar parametros'.  

Podemos alojar este comando en una subcarpeta dedicada a ajustes avanzados, ya sea dentro del PartWorkbench o en el directorio global que estén manejando para preferencias. Te dejo la estructura estándar:

Ubicación sugerida: tickets/DAV_Diccionario/PartWorkbench/fine_tuning/

Archivo 1: fine_tuning.py
Python

# Copyright (C) 2026 El Equipo del Proyecto DAV
# Universidad Autónoma de Entre Ríos (UADER)
# Bajo la dirección de Guillermo Gerard y Gallo Fabricio David
#
# Este programa es software libre: usted puede redistribuirlo y/o modificarlo
# bajo los términos de la Licencia Pública General GNU tal como fue publicada
# por la Fundación para el Software Libre, en la versión 3 de la Licencia.
#
# Este programa se distribuye con la esperanza de que sea útil,
# pero SIN NINGUNA GARANTÍA; incluso sin la garantía implícita de
# MERCANTIBILIDAD o APTITUD PARA UN PROPÓSITO PARTICULAR. Consulte la
# Licencia Pública General GNU para más detalles.
#
# Deberías haber recibido una copia de la Licencia Pública General GNU
# junto con este programa. Si no es así, consulte <http://www.gnu.org/licenses/>.

import FreeCADGui as Gui
from .ayuda import ayuda


fine_tuning = {
    'fine tuning': lambda: Gui.runCommand('Std_DlgParameter', 0),
    'configuracion avanzada': lambda: Gui.runCommand('Std_DlgParameter', 0),
    'modificar parametros': lambda: Gui.runCommand('Std_DlgParameter', 0),
    'help': ayuda,
}

Archivo 2: ayuda.py
Python

# Copyright (C) 2026 El Equipo del Proyecto DAV
# Universidad Autónoma de Entre Ríos (UADER)
# Bajo la dirección de Guillermo Gerard y Gallo Fabricio David
#
# Este programa es software libre: usted puede redistribuirlo y/o modificarlo
# bajo los términos de la Licencia Pública General GNU tal como fue publicada
# por la Fundación para el Software Libre, en la versión 3 de la Licencia.
#
# Este programa se distribuye con la esperanza de que sea útil,
# pero SIN NINGUNA GARANTÍA; incluso sin la garantía implícita de
# MERCANTIBILIDAD o APTITUD PARA UN PROPÓSITO PARTICULAR. Consulte la
# Licencia Pública General GNU para más detalles.
#
# Deberías haber recibido una copia de la Licencia Pública General GNU
# junto con este programa. Si no es así, consulte <http://www.gnu.org/licenses/>.


def ayuda():
    print('Comandos disponibles en este nivel:')
    print('  fine tuning / configuracion avanzada / modificar parametros - Abre el Parameter Editor.')
    print('         Requiere: Conocimientos básicos sobre parámetros internos (ubicados en BaseApp/Preferences/).')
    print('         Devuelve: Una interfaz para editar manualmente parámetros avanzados.')
    print('         Nota: Permite ajustar configuraciones de interfaz, navegación, workbenches y atajos.')
    print('               Algunos cambios requieren reiniciar FreeCAD para aplicarse correctamente.')

El diccionario para el Parameter Editor ya quedó configurado y la advertencia sobre el reinicio del software quedó documentada en el ayuda.py. ¡Pasame el próximo ticket (veo que faltan los de Import/Export y los de Assembly) para continuar!  

ticket importExport-preferences

¡Recibido el ticket de ImportExport Preferences!

Al igual que en los tickets de PartDesign Preferences y Fine Tuning, el texto nos indica la ruta de la interfaz gráfica (Edit → Preferences → Import-Export) en lugar del script. Como en FreeCAD la ventana de preferencias se maneja de forma centralizada, el comando correcto para abrirla desde Python y que el usuario interactúe con ella es Gui.runCommand('Std_DlgPreferences', 0).

Para las palabras clave sugeridas, las normalizaremos quitando tildes y dejándolas en minúsculas para el motor Vosk. Nos quedarán: 'import export preferences', 'configuracion importacion exportacion', 'preferencias dxf', 'preferencias step', 'configuracion ifc' y 'export settings'.

Ubicaremos estos comandos en una subcarpeta de importación/exportación dentro de la estructura.

Ubicación sugerida: tickets/DAV_Diccionario/PartWorkbench/import_export/

Archivo 1: import_export.py
Python

# Copyright (C) 2026 El Equipo del Proyecto DAV
# Universidad Autónoma de Entre Ríos (UADER)
# Bajo la dirección de Guillermo Gerard y Gallo Fabricio David
#
# Este programa es software libre: usted puede redistribuirlo y/o modificarlo
# bajo los términos de la Licencia Pública General GNU tal como fue publicada
# por la Fundación para el Software Libre, en la versión 3 de la Licencia.
#
# Este programa se distribuye con la esperanza de que sea útil,
# pero SIN NINGUNA GARANTÍA; incluso sin la garantía implícita de
# MERCANTIBILIDAD o APTITUD PARA UN PROPÓSITO PARTICULAR. Consulte la
# Licencia Pública General GNU para más detalles.
#
# Deberías haber recibido una copia de la Licencia Pública General GNU
# junto con este programa. Si no es así, consulte <http://www.gnu.org/licenses/>.

import FreeCADGui as Gui
from .ayuda import ayuda


import_export = {
    'import export preferences': lambda: Gui.runCommand('Std_DlgPreferences', 0),
    'configuracion importacion exportacion': lambda: Gui.runCommand('Std_DlgPreferences', 0),
    'preferencias dxf': lambda: Gui.runCommand('Std_DlgPreferences', 0),
    'preferencias step': lambda: Gui.runCommand('Std_DlgPreferences', 0),
    'configuracion ifc': lambda: Gui.runCommand('Std_DlgPreferences', 0),
    'export settings': lambda: Gui.runCommand('Std_DlgPreferences', 0),
    'help': ayuda,
}

Archivo 2: ayuda.py
Python

# Copyright (C) 2026 El Equipo del Proyecto DAV
# Universidad Autónoma de Entre Ríos (UADER)
# Bajo la dirección de Guillermo Gerard y Gallo Fabricio David
#
# Este programa es software libre: usted puede redistribuirlo y/o modificarlo
# bajo los términos de la Licencia Pública General GNU tal como fue publicada
# por la Fundación para el Software Libre, en la versión 3 de la Licencia.
#
# Este programa se distribuye con la esperanza de que sea útil,
# pero SIN NINGUNA GARANTÍA; incluso sin la garantía implícita de
# MERCANTIBILIDAD o APTITUD PARA UN PROPÓSITO PARTICULAR. Consulte la
# Licencia Pública General GNU para más detalles.
#
# Deberías haber recibido una copia de la Licencia Pública General GNU
# junto con este programa. Si no es así, consulte <http://www.gnu.org/licenses/>.


def ayuda():
    print('Comandos disponibles en este nivel:')
    print('  configuracion importacion exportacion / preferencias dxf / etc - Abre la ventana de preferencias de importación y exportación.')
    print('         Requiere: Tener cargado el workbench correspondiente según el formato a utilizar[cite: 72].')
    print('         Devuelve: Una interfaz de configuración para controlar parámetros de múltiples formatos CAD y BIM[cite: 74].')
    print('         Nota: Incluye opciones para DAE, DWG, DXF, IFC, IGES, STEP, SVG y VTK[cite: 75].')
    print('               Algunas preferencias dependen de módulos externos como pyCollada o IfcOpenShell[cite: 76].')

Con este ticket listo, el bloque de preferencias generales queda cubierto. ¡Pasame los tickets de AssemblyWorkbench que te queden en la lista para continuar la tarea!

Ahora siguen los tickets del diccionario de AssemblyWorkBench

¡Excelente! Empezamos con el AssemblyWorkbench.

Al analizar el ticket de Assembly_CreateJointAngle, vemos que el script sugerido (Gui.runCommand('Assembly_CreateJointAngle', 0)) es perfectamente válido, ya que abre el panel de tareas para que el usuario pueda configurar la unión y el ángulo específico.  

Las palabras clave sugeridas son varias. Siguiendo las reglas de normalización para Vosk, les quitaremos las tildes y las dejaremos en minúsculas. Omitiremos la opción "ángulo" + [valor en grados] como clave estricta, ya que Vosk requiere frases exactas en el diccionario, y si el usuario dicta el valor, el motor de voz lo procesará como parte de la cadena; por ende, dejaremos las frases base para que invoquen el panel de tareas. Las claves quedarán: 'crear union de angulo', 'union de angulo', 'restriccion de angulo', 'angulo entre piezas' y 'joint de angulo'.  

Vamos a crear la subcarpeta correspondiente dentro de AssemblyWorkbench.

Ubicación: tickets/DAV_Diccionario/AssemblyWorkbench/create_joint_angle/

Archivo 1: create_joint_angle.py
Python

# Copyright (C) 2026 El Equipo del Proyecto DAV
# Universidad Autónoma de Entre Ríos (UADER)
# Bajo la dirección de Guillermo Gerard y Gallo Fabricio David
#
# Este programa es software libre: usted puede redistribuirlo y/o modificarlo
# bajo los términos de la Licencia Pública General GNU tal como fue publicada
# por la Fundación para el Software Libre, en la versión 3 de la Licencia.
#
# Este programa se distribuye con la esperanza de que sea útil,
# pero SIN NINGUNA GARANTÍA; incluso sin la garantía implícita de
# MERCANTIBILIDAD o APTITUD PARA UN PROPÓSITO PARTICULAR. Consulte la
# Licencia Pública General GNU para más detalles.
#
# Deberías haber recibido una copia de la Licencia Pública General GNU
# junto con este programa. Si no es así, consulte <http://www.gnu.org/licenses/>.

import FreeCADGui as Gui
from .ayuda import ayuda


create_joint_angle = {
    'crear union de angulo': lambda: Gui.runCommand('Assembly_CreateJointAngle', 0),
    'union de angulo': lambda: Gui.runCommand('Assembly_CreateJointAngle', 0),
    'restriccion de angulo': lambda: Gui.runCommand('Assembly_CreateJointAngle', 0),
    'angulo entre piezas': lambda: Gui.runCommand('Assembly_CreateJointAngle', 0),
    'joint de angulo': lambda: Gui.runCommand('Assembly_CreateJointAngle', 0),
    'help': ayuda,
}

Archivo 2: ayuda.py
Python

# Copyright (C) 2026 El Equipo del Proyecto DAV
# Universidad Autónoma de Entre Ríos (UADER)
# Bajo la dirección de Guillermo Gerard y Gallo Fabricio David
#
# Este programa es software libre: usted puede redistribuirlo y/o modificarlo
# bajo los términos de la Licencia Pública General GNU tal como fue publicada
# por la Fundación para el Software Libre, en la versión 3 de la Licencia.
#
# Este programa se distribuye con la esperanza de que sea útil,
# pero SIN NINGUNA GARANTÍA; incluso sin la garantía implícita de
# MERCANTIBILIDAD o APTITUD PARA UN PROPÓSITO PARTICULAR. Consulte la
# Licencia Pública General GNU para más detalles.
#
# Deberías haber recibido una copia de la Licencia Pública General GNU
# junto con este programa. Si no es así, consulte <http://www.gnu.org/licenses/>.


def ayuda():
    print('Comandos disponibles en este nivel:')
    print('  crear union de angulo / union de angulo / restriccion de angulo - Crea una restricción de ángulo entre dos entidades geométricas.')
    print('         Requiere: Workbench Assembly activo y un Ensamblaje activo.')
    print('                   Opcionalmente, dos entidades geométricas preseleccionadas (caras planas o aristas lineales).')
    print('         Devuelve: Abre el panel de tareas de uniones. Crea un objeto Angle bajo el contenedor Joints.')
    print('         Nota: Fuerza un ángulo específico entre dos piezas distintas del ensamblaje.')

Ya tenemos el primer comando del módulo de ensamblaje. ¡Pasame el próximo ticket!

ticket assembly_createjoinbelt

¡Recibido el ticket de Assembly_CreateJointBelt!

Al analizar este ticket, notamos una precondición fundamental para el funcionamiento correcto de esta herramienta en el entorno de FreeCAD: es un requisito obligatorio que existan previamente dos Revolute joints en el ensamblaje, ya que este comando no crea geometría, sino que acopla cinemáticamente esas dos rotaciones en el mismo sentido. Como bien advierte el ticket, esto permite simular transmisiones por correa o cadena. Si el usuario invoca el comando sin estos prerrequisitos, la herramienta no podrá cumplir su función. Por lo tanto, dejaremos esta advertencia bien clara en el archivo de ayuda.  

En cuanto al script nativo, la ejecución mediante Gui.runCommand('Assembly_CreateJointBelt', 0) es la correcta.  

Normalizamos las palabras sugeridas para los comandos de voz quitando las tildes y dejándolas en minúsculas. Nos quedarán: 'crear union de correa', 'union de correa', 'belt joint', 'joint de correa', 'transmision por correa', 'correa de transmision' y 'cadena'.  

Procedemos a armar la estructura en su subcarpeta dentro del AssemblyWorkbench.

Ubicación: tickets/DAV_Diccionario/AssemblyWorkbench/create_joint_belt/

Archivo 1: create_joint_belt.py
Python

# Copyright (C) 2026 El Equipo del Proyecto DAV
# Universidad Autónoma de Entre Ríos (UADER)
# Bajo la dirección de Guillermo Gerard y Gallo Fabricio David
#
# Este programa es software libre: usted puede redistribuirlo y/o modificarlo
# bajo los términos de la Licencia Pública General GNU tal como fue publicada
# por la Fundación para el Software Libre, en la versión 3 de la Licencia.
#
# Este programa se distribuye con la esperanza de que sea útil,
# pero SIN NINGUNA GARANTÍA; incluso sin la garantía implícita de
# MERCANTIBILIDAD o APTITUD PARA UN PROPÓSITO PARTICULAR. Consulte la
# Licencia Pública General GNU para más detalles.
#
# Deberías haber recibido una copia de la Licencia Pública General GNU
# junto con este programa. Si no es así, consulte <http://www.gnu.org/licenses/>.

import FreeCADGui as Gui
from .ayuda import ayuda


create_joint_belt = {
    'crear union de correa': lambda: Gui.runCommand('Assembly_CreateJointBelt', 0),
    'union de correa': lambda: Gui.runCommand('Assembly_CreateJointBelt', 0),
    'belt joint': lambda: Gui.runCommand('Assembly_CreateJointBelt', 0),
    'joint de correa': lambda: Gui.runCommand('Assembly_CreateJointBelt', 0),
    'transmision por correa': lambda: Gui.runCommand('Assembly_CreateJointBelt', 0),
    'correa de transmision': lambda: Gui.runCommand('Assembly_CreateJointBelt', 0),
    'cadena': lambda: Gui.runCommand('Assembly_CreateJointBelt', 0),
    'help': ayuda,
}

Archivo 2: ayuda.py
Python

# Copyright (C) 2026 El Equipo del Proyecto DAV
# Universidad Autónoma de Entre Ríos (UADER)
# Bajo la dirección de Guillermo Gerard y Gallo Fabricio David
#
# Este programa es software libre: usted puede redistribuirlo y/o modificarlo
# bajo los términos de la Licencia Pública General GNU tal como fue publicada
# por la Fundación para el Software Libre, en la versión 3 de la Licencia.
#
# Este programa se distribuye con la esperanza de que sea útil,
# pero SIN NINGUNA GARANTÍA; incluso sin la garantía implícita de
# MERCANTIBILIDAD o APTITUD PARA UN PROPÓSITO PARTICULAR. Consulte la
# Licencia Pública General GNU para más detalles.
#
# Deberías haber recibido una copia de la Licencia Pública General GNU
# junto con este programa. Si no es así, consulte <http://www.gnu.org/licenses/>.


def ayuda():
    print('Comandos disponibles en este nivel:')
    print('  crear union de correa / cadena / transmision por correa - Crea una unión de correa o cadena (belt joint).')
    print('         Requiere: Workbench Assembly activo y un Ensamblaje activo.')
    print('                   REQUISITO OBLIGATORIO: Deben existir previamente dos Revolute joints en el ensamblaje.')
    print('         Devuelve: Abre el panel de tareas para configurar radios. Crea un objeto Belt bajo Joints.')
    print('         Nota: Acopla la rotación de dos piezas en el MISMO sentido. No crea la geometría de la correa, solo el acoplamiento cinemático.')

El diccionario para la unión de correa ha quedado configurado. ¡Pasame el próximo ticket de la lista para continuar!

ticket assemblycreatejoingears

¡Recibido! Al analizar el contenido del ticket, veo que corresponde a Assembly_CreateJointScrew  (aunque al final de tu mensaje anotaste "gears", procesaremos el del husillo que es el texto proporcionado).  

Al igual que con la unión de correa que vimos antes, esta herramienta de transmisión tiene un prerrequisito estricto: requiere obligatoriamente que existan de antemano un Slider joint y un Revolute joint en el ensamblaje activo. La función de este comando no es crear las piezas, sino acoplar la traslación de la primera con la rotación de la segunda para simular un tornillo de avance. Debido a que la herramienta fallará si estos prerrequisitos no se cumplen, lo dejaremos muy claro en las advertencias del archivo de ayuda.  

Para la integración con el motor de voz Vosk, tomaremos las sugerencias del ticket  y las normalizaremos estandarizándolas en minúsculas y sin tildes. El script nativo a utilizar para abrir el panel de configuración será la llamada a la interfaz gráfica: Gui.runCommand('Assembly_CreateJointScrew', 0).  

A continuación, la estructura para su subcarpeta dentro del AssemblyWorkbench.

Ubicación: tickets/DAV_Diccionario/AssemblyWorkbench/create_joint_screw/

Archivo 1: create_joint_screw.py
Python

# Copyright (C) 2026 El Equipo del Proyecto DAV
# Universidad Autónoma de Entre Ríos (UADER)
# Bajo la dirección de Guillermo Gerard y Gallo Fabricio David
#
# Este programa es software libre: usted puede redistribuirlo y/o modificarlo
# bajo los términos de la Licencia Pública General GNU tal como fue publicada
# por la Fundación para el Software Libre, en la versión 3 de la Licencia.
#
# Este programa se distribuye con la esperanza de que sea útil,
# pero SIN NINGUNA GARANTÍA; incluso sin la garantía implícita de
# MERCANTIBILIDAD o APTITUD PARA UN PROPÓSITO PARTICULAR. Consulte la
# Licencia Pública General GNU para más detalles.
#
# Deberías haber recibido una copia de la Licencia Pública General GNU
# junto con este programa. Si no es así, consulte <http://www.gnu.org/licenses/>.

import FreeCADGui as Gui
from .ayuda import ayuda


create_joint_screw = {
    'crear union helicoidal': lambda: Gui.runCommand('Assembly_CreateJointScrew', 0),
    'union helicoidal': lambda: Gui.runCommand('Assembly_CreateJointScrew', 0),
    'joint de tornillo': lambda: Gui.runCommand('Assembly_CreateJointScrew', 0),
    'tornillo de avance': lambda: Gui.runCommand('Assembly_CreateJointScrew', 0),
    'screw joint': lambda: Gui.runCommand('Assembly_CreateJointScrew', 0),
    'husillo': lambda: Gui.runCommand('Assembly_CreateJointScrew', 0),
    'help': ayuda,
}

Archivo 2: ayuda.py
Python

# Copyright (C) 2026 El Equipo del Proyecto DAV
# Universidad Autónoma de Entre Ríos (UADER)
# Bajo la dirección de Guillermo Gerard y Gallo Fabricio David
#
# Este programa es software libre: usted puede redistribuirlo y/o modificarlo
# bajo los términos de la Licencia Pública General GNU tal como fue publicada
# por la Fundación para el Software Libre, en la versión 3 de la Licencia.
#
# Este programa se distribuye con la esperanza de que sea útil,
# pero SIN NINGUNA GARANTÍA; incluso sin la garantía implícita de
# MERCANTIBILIDAD o APTITUD PARA UN PROPÓSITO PARTICULAR. Consulte la
# Licencia Pública General GNU para más detalles.
#
# Deberías haber recibido una copia de la Licencia Pública General GNU
# junto con este programa. Si no es así, consulte <http://www.gnu.org/licenses/>.


def ayuda():
    print('Comandos disponibles en este nivel:')
    print('  crear union helicoidal / husillo / tornillo de avance - Crea una unión helicoidal (screw joint).')
    print('         Requiere: Workbench Assembly y Ensamblaje activos.')
    print('                   REQUISITO OBLIGATORIO: Debe existir previamente un Slider joint y un Revolute joint.')
    print('         Devuelve: Abre el panel de tareas para configurar el paso (pitch). Crea un objeto Screw bajo Joints.')
    print('         Nota: Simula un tornillo de avance, acoplando la traslación de un componente con la rotación del otro.')

El diccionario para la unión helicoidal quedó listo y seguro. ¡Pasame el próximo ticket (como el de Gears que mencionaste) para que sigamos!

 ticket assemblycreatejoingears

¡Recibido el ticket de Assembly_CreateJointGears!

Al analizar este ticket, vemos que sigue la misma lógica estricta que la unión de correa y la unión helicoidal: tiene como requisito obligatorio que existan previamente dos Revolute joints en el ensamblaje, uno por cada engranaje. Es crucial entender que este comando no crea la geometría de los engranajes, sino que sólo impone el acoplamiento cinemático entre dos piezas que ya rotan. Dejaremos esta advertencia bien clara en la función de ayuda para que el usuario sepa que, si faltan estos prerrequisitos, el comando no funcionará.  

Para las palabras clave, el ticket sugiere varias frases. Las normalizaremos quitando tildes y dejándolas completamente en minúsculas para cumplir con los requerimientos del motor Vosk. El script nativo a utilizar es la llamada a la interfaz gráfica: Gui.runCommand('Assembly_CreateJointGears', 0).  

A continuación, te presento la estructura para su subcarpeta dentro del AssemblyWorkbench.

Ubicación: tickets/DAV_Diccionario/AssemblyWorkbench/create_joint_gears/

Archivo 1: create_joint_gears.py
Python

# Copyright (C) 2026 El Equipo del Proyecto DAV
# Universidad Autónoma de Entre Ríos (UADER)
# Bajo la dirección de Guillermo Gerard y Gallo Fabricio David
#
# Este programa es software libre: usted puede redistribuirlo y/o modificarlo
# bajo los términos de la Licencia Pública General GNU tal como fue publicada
# por la Fundación para el Software Libre, en la versión 3 de la Licencia.
#
# Este programa se distribuye con la esperanza de que sea útil,
# pero SIN NINGUNA GARANTÍA; incluso sin la garantía implícita de
# MERCANTIBILIDAD o APTITUD PARA UN PROPÓSITO PARTICULAR. Consulte la
# Licencia Pública General GNU para más detalles.
#
# Deberías haber recibido una copia de la Licencia Pública General GNU
# junto con este programa. Si no es así, consulte <http://www.gnu.org/licenses/>.

import FreeCADGui as Gui
from .ayuda import ayuda


create_joint_gears = {
    'crear union de engranajes': lambda: Gui.runCommand('Assembly_CreateJointGears', 0),
    'union de engranajes': lambda: Gui.runCommand('Assembly_CreateJointGears', 0),
    'gears joint': lambda: Gui.runCommand('Assembly_CreateJointGears', 0),
    'joint de engranajes': lambda: Gui.runCommand('Assembly_CreateJointGears', 0),
    'acoplar engranajes': lambda: Gui.runCommand('Assembly_CreateJointGears', 0),
    'transmision por engranajes': lambda: Gui.runCommand('Assembly_CreateJointGears', 0),
    'help': ayuda,
}

Archivo 2: ayuda.py
Python

# Copyright (C) 2026 El Equipo del Proyecto DAV
# Universidad Autónoma de Entre Ríos (UADER)
# Bajo la dirección de Guillermo Gerard y Gallo Fabricio David
#
# Este programa es software libre: usted puede redistribuirlo y/o modificarlo
# bajo los términos de la Licencia Pública General GNU tal como fue publicada
# por la Fundación para el Software Libre, en la versión 3 de la Licencia.
#
# Este programa se distribuye con la esperanza de que sea útil,
# pero SIN NINGUNA GARANTÍA; incluso sin la garantía implícita de
# MERCANTIBILIDAD o APTITUD PARA UN PROPÓSITO PARTICULAR. Consulte la
# Licencia Pública General GNU para más detalles.
#
# Deberías haber recibido una copia de la Licencia Pública General GNU
# junto con este programa. Si no es así, consulte <http://www.gnu.org/licenses/>.


def ayuda():
    print('Comandos disponibles en este nivel:')
    print('  crear union de engranajes / union de engranajes / acoplar engranajes - Crea una unión de engranajes (gears joint).')
    print('         Requiere: Workbench Assembly activo y un Ensamblaje activo.')
    print('                   REQUISITO OBLIGATORIO: Deben existir previamente dos Revolute joints en el ensamblaje.')
    print('         Devuelve: Abre el panel de tareas para configurar radios de paso. Crea un objeto Gears bajo Joints.')
    print('         Nota: No crea la geometría, sólo impone el acoplamiento cinemático entre dos piezas que ya rotan.')

El diccionario para la unión de engranajes ya quedó configurado. ¡Pasame el próximo ticket cuando estés listo!

ticket togglegraunded

¡Recibido el último ticket de tu lista, Assembly_ToggleGrounded!   

Al analizar este comando, vemos que es una acción directa sobre la selección activa (sin panel de tareas) que fija la posición y orientación de una o más piezas. Actúa como un anclaje, inmovilizando la pieza para que no pueda ser desplazada por el solver. Es fundamental documentar que este es el paso previo obligatorio en cualquier flujo de ensamblaje: siempre se debe anclar al menos una pieza base antes de agregar uniones (joints) a las demás. Además, requiere que el usuario tenga al menos una pieza seleccionada antes de ejecutarlo.  

Para la integración con el motor de voz Vosk, normalizamos las palabras sugeridas quitando mayúsculas y tildes. Las claves quedarán como: 'anclar pieza', 'fijar pieza', 'inmovilizar pieza', 'toggle grounded' y 'bloquear posicion'.  

Aquí tienes la estructura final para esta subcarpeta dentro del AssemblyWorkbench.

Ubicación: tickets/DAV_Diccionario/AssemblyWorkbench/toggle_grounded/

Archivo 1: toggle_grounded.py
Python

# Copyright (C) 2026 El Equipo del Proyecto DAV
# Universidad Autónoma de Entre Ríos (UADER)
# Bajo la dirección de Guillermo Gerard y Gallo Fabricio David
#
# Este programa es software libre: usted puede redistribuirlo y/o modificarlo
# bajo los términos de la Licencia Pública General GNU tal como fue publicada
# por la Fundación para el Software Libre, en la versión 3 de la Licencia.
#
# Este programa se distribuye con la esperanza de que sea útil,
# pero SIN NINGUNA GARANTÍA; incluso sin la garantía implícita de
# MERCANTIBILIDAD o APTITUD PARA UN PROPÓSITO PARTICULAR. Consulte la
# Licencia Pública General GNU para más detalles.
#
# Deberías haber recibido una copia de la Licencia Pública General GNU
# junto con este programa. Si no es así, consulte <http://www.gnu.org/licenses/>.

import FreeCADGui as Gui
from .ayuda import ayuda


toggle_grounded = {
    'anclar pieza': lambda: Gui.runCommand('Assembly_ToggleGrounded', 0),
    'fijar pieza': lambda: Gui.runCommand('Assembly_ToggleGrounded', 0),
    'inmovilizar pieza': lambda: Gui.runCommand('Assembly_ToggleGrounded', 0),
    'toggle grounded': lambda: Gui.runCommand('Assembly_ToggleGrounded', 0),
    'bloquear posicion': lambda: Gui.runCommand('Assembly_ToggleGrounded', 0),
    'help': ayuda,
}

Archivo 2: ayuda.py
Python

# Copyright (C) 2026 El Equipo del Proyecto DAV
# Universidad Autónoma de Entre Ríos (UADER)
# Bajo la dirección de Guillermo Gerard y Gallo Fabricio David
#
# Este programa es software libre: usted puede redistribuirlo y/o modificarlo
# bajo los términos de la Licencia Pública General GNU tal como fue publicada
# por la Fundación para el Software Libre, en la versión 3 de la Licencia.
#
# Este programa se distribuye con la esperanza de que sea útil,
# pero SIN NINGUNA GARANTÍA; incluso sin la garantía implícita de
# MERCANTIBILIDAD o APTITUD PARA UN PROPÓSITO PARTICULAR. Consulte la
# Licencia Pública General GNU para más detalles.
#
# Deberías haber recibido una copia de la Licencia Pública General GNU
# junto con este programa. Si no es así, consulte <http://www.gnu.org/licenses/>.


def ayuda():
    print('Comandos disponibles en este nivel:')
    print('  anclar pieza / fijar pieza / inmovilizar pieza - Fija la posición y orientación de una o más piezas.')
    print('         Requiere: Workbench Assembly y Ensamblaje activos. Al menos una pieza seleccionada.')
    print('         Devuelve: Crea un objeto GroundedJoint. La pieza queda inmovilizada.')
    print('         Nota: Es el paso previo obligatorio en un flujo de ensamblaje (anclar una pieza base). Ejecutar de nuevo desactiva el anclaje.')

¡Con esto hemos completado los 25 tickets que tenías asignados para armar los diccionarios! Ya tenés todas las carpetas, los subdiccionarios y los archivos de ayuda listos para integrarse al repositorio del proyecto y empezar a probarlos con el motor Vosk en tu entorno de desarrollo. Si surge algún otro módulo o necesitás revisar la lógica de las funciones, quedo a disposición. ¡Mucho éxito con la cursada y con el avance de este excelente proyecto inclusivo!
Concordia, Entre Ríos, Argentina  • Actualizar ubicación


Gemini es una IA y puede cometer errores. 