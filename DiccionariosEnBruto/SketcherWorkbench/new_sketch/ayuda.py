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
