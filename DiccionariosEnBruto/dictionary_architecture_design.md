# Dictionary Architecture Design

This document outlines the logical architecture of the FreeCAD voice command dictionaries for the DAV project.

```text
# Estructura Lógica de Diccionarios DAV

DAV_Diccionario/
│
├── PartWorkbench/                      (Módulo Principal de Modelado)
│   │
│   ├── Primitives/                     (Subconjunto: Formas Base)
│   │   ├── elipsoide                   [Ellipsoid]
│   │   ├── helice                      [Helix]
│   │   └── cuna                        [Wedge]
│   │
│   ├── Modificadores_3D/               (Subconjunto: Operaciones Sólidas)
│   │   ├── loft                        [Part_Loft]
│   │   ├── desfase                     [Part_Offset]
│   │   ├── revolucion                  [Part_Revolve]
│   │   ├── escalar                     [Part_Scale]
│   │   ├── barrer_perfil               [Part_Sweep]
│   │   └── dar_espesor                 [Part_Thickness]
│   │
│   ├── Modificadores_2D_y_Superficies/ (Subconjunto: Operaciones Planas)
│   │   ├── crear_cara                  [Part_MakeFace]
│   │   ├── contorno                    [Part_Offset2D]
│   │   ├── proyectar_dibujo            [Part_ProjectionOnSurface]
│   │   └── unir_curvas                 [Part_RuledSurface]
│   │
│   ├── Intersecciones_y_Cortes/        (Subconjunto: Análisis y Geometría)
│   │   ├── secciones_transversales     [Part_CrossSections]
│   │   └── obtener_seccion             [Part_Section]
│   │
│   └── Preferencias_y_Ajustes/         (Subconjunto: Configuración del Sistema)
│       ├── preferencias_part           [PartDesign Preferences]
│       ├── fine_tuning                 [Fine Tuning]
│       └── import_export               [ImportExport Preferences]
│
├── AssemblyWorkbench/                  (Módulo Principal de Ensamblaje)
│   │
│   ├── Joints_de_Transmision/          (Subconjunto: Movimiento Acoplado)
│   │   ├── union_correa                [Assembly_CreateJointBelt]
│   │   ├── union_engranajes            [Assembly_CreateJointGears]
│   │   └── union_helicoidal            [Assembly_CreateJointScrew]
│   │
│   ├── Joints_Estaticos/               (Subconjunto: Restricciones Fijas)
│   │   └── union_angulo                [Assembly_CreateJointAngle]
│   │
│   └── Anclajes/                       (Subconjunto: Fijación de Piezas)
│       └── anclar_pieza                [Assembly_ToggleGrounded]
│
└── SketcherWorkbench/                  (Módulo Principal de Bocetos)
    │
    └── Operaciones_Base/               (Subconjunto: Inicio de flujos 2D)
        └── nuevo_boceto                [Sketcher_NewSketch]
```
