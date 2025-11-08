Perfecto ✅
Esta **segunda parte** continúa el proyecto **Costco (UIII_Costco_0599)** en **Django**, pero ahora trabajarás con el **modelo: PRODUCTO**.
Te dejo **todo paso a paso**, con el código completo, vistas CRUD, URLs, plantillas y ajustes del navbar.

---

## 🧩 Parte 2 — CRUD de PRODUCTO

---

### **1️⃣ Modificar el modelo `Producto` para agregar imagen mediante URL**

Archivo: `app_Costco/models.py`

Reemplaza la clase `Producto` por esta versión (solo agregamos el campo `imagen_url`):

```python
class Producto(models.Model):
    # Campos de Producto
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    categoria = models.CharField(max_length=100, blank=True, null=True)
    codigo_barras = models.CharField(max_length=50, unique=True, blank=True, null=True)
    imagen_url = models.URLField(blank=True, null=True)  # Nuevo campo
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
```

---

### **2️⃣ Realizar migraciones**

Ejecuta en la terminal dentro del entorno virtual:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### **3️⃣ Ahora trabajamos con el MODELO: PRODUCTO**

Crearemos vistas CRUD completas sin usar `forms.py`.

---

### **4️⃣ Crear las funciones de vista en `app_Costco/views.py`**

Agrega este código (debajo de las vistas de `Usuario`):

```python
from .models import Producto

# Agregar producto
def agregar_producto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        precio = request.POST.get('precio')
        stock = request.POST.get('stock')
        categoria = request.POST.get('categoria')
        codigo_barras = request.POST.get('codigo_barras')
        imagen_url = request.POST.get('imagen_url')

        Producto.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            precio=precio,
            stock=stock,
            categoria=categoria,
            codigo_barras=codigo_barras,
            imagen_url=imagen_url
        )
        return redirect('ver_producto')
    return render(request, 'producto/agregar_producto.html')


# Ver productos
def ver_producto(request):
    productos = Producto.objects.all().order_by('-fecha_creacion')
    return render(request, 'producto/ver_producto.html', {'productos': productos})


# Mostrar formulario de actualización
def actualizar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    return render(request, 'producto/actualizar_producto.html', {'producto': producto})


# Realizar actualización
def realizar_actualizacion_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        producto.nombre = request.POST.get('nombre')
        producto.descripcion = request.POST.get('descripcion')
        producto.precio = request.POST.get('precio')
        producto.stock = request.POST.get('stock')
        producto.categoria = request.POST.get('categoria')
        producto.codigo_barras = request.POST.get('codigo_barras')
        producto.imagen_url = request.POST.get('imagen_url')
        producto.save()
        return redirect('ver_producto')
    return redirect('actualizar_producto', producto_id=producto_id)


# Borrar producto
def borrar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        producto.delete()
        return redirect('ver_producto')
    return render(request, 'producto/borrar_producto.html', {'producto': producto})
```

---

### **5️⃣ Modificar el archivo `navbar.html`**

Archivo: `app_Costco/templates/navbar.html`

Reemplaza el bloque de **Productos** por este actualizado:

```html
<li class="nav-item dropdown">
  <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown">
    Productos
  </a>
  <ul class="dropdown-menu">
    <li><a class="dropdown-item" href="{% url 'agregar_producto' %}">Agregar producto</a></li>
    <li><a class="dropdown-item" href="{% url 'ver_producto' %}">Ver productos</a></li>
    <li><a class="dropdown-item" href="#">Actualizar producto</a></li>
    <li><a class="dropdown-item" href="#">Borrar producto</a></li>
  </ul>
</li>
```

---

### **6️⃣ Crear subcarpeta `producto` dentro de templates**

Ruta completa:

```
app_Costco/templates/producto/
```

---

### **7️⃣ Crear archivos HTML (CRUD PRODUCTO)**

#### 📄 `agregar_producto.html`

```html
{% extends "base.html" %}
{% block content %}
<h2>Agregar Producto</h2>
<form method="post">
  {% csrf_token %}
  <div class="mb-3">
    <label class="form-label">Nombre</label>
    <input class="form-control" name="nombre">
  </div>
  <div class="mb-3">
    <label class="form-label">Descripción</label>
    <textarea class="form-control" name="descripcion"></textarea>
  </div>
  <div class="mb-3">
    <label class="form-label">Precio</label>
    <input class="form-control" name="precio" type="number" step="0.01">
  </div>
  <div class="mb-3">
    <label class="form-label">Stock</label>
    <input class="form-control" name="stock" type="number">
  </div>
  <div class="mb-3">
    <label class="form-label">Categoría</label>
    <input class="form-control" name="categoria">
  </div>
  <div class="mb-3">
    <label class="form-label">Código de barras</label>
    <input class="form-control" name="codigo_barras">
  </div>
  <div class="mb-3">
    <label class="form-label">URL de imagen</label>
    <input class="form-control" name="imagen_url" type="url">
  </div>
  <button class="btn btn-primary">Guardar</button>
  <a class="btn btn-secondary" href="{% url 'ver_producto' %}">Cancelar</a>
</form>
{% endblock %}
```

---

#### 📄 `ver_producto.html`

```html
{% extends "base.html" %}
{% block content %}
<h2>Lista de Productos</h2>
<a class="btn btn-success mb-3" href="{% url 'agregar_producto' %}">+ Agregar Producto</a>
<table class="table table-hover">
  <thead>
    <tr>
      <th>ID</th>
      <th>Imagen</th>
      <th>Nombre</th>
      <th>Precio</th>
      <th>Stock</th>
      <th>Categoría</th>
      <th>Acciones</th>
    </tr>
  </thead>
  <tbody>
    {% for p in productos %}
    <tr>
      <td>{{ p.id }}</td>
      <td>
        {% if p.imagen_url %}
          <img src="{{ p.imagen_url }}" width="60" height="60" style="object-fit:cover;">
        {% else %}
          <span class="text-muted">Sin imagen</span>
        {% endif %}
      </td>
      <td>{{ p.nombre }}</td>
      <td>${{ p.precio }}</td>
      <td>{{ p.stock }}</td>
      <td>{{ p.categoria }}</td>
      <td>
        <a class="btn btn-sm btn-info" href="{% url 'actualizar_producto' p.id %}">Editar</a>
        <a class="btn btn-sm btn-danger" href="{% url 'borrar_producto' p.id %}">Borrar</a>
      </td>
    </tr>
    {% empty %}
    <tr><td colspan="7">No hay productos.</td></tr>
    {% endfor %}
  </tbody>
</table>
{% endblock %}
```

---

#### 📄 `actualizar_producto.html`

```html
{% extends "base.html" %}
{% block content %}
<h2>Actualizar Producto</h2>
<form method="post" action="{% url 'realizar_actualizacion_producto' producto.id %}">
  {% csrf_token %}
  <div class="mb-3">
    <label class="form-label">Nombre</label>
    <input class="form-control" name="nombre" value="{{ producto.nombre }}">
  </div>
  <div class="mb-3">
    <label class="form-label">Descripción</label>
    <textarea class="form-control" name="descripcion">{{ producto.descripcion }}</textarea>
  </div>
  <div class="mb-3">
    <label class="form-label">Precio</label>
    <input class="form-control" name="precio" value="{{ producto.precio }}">
  </div>
  <div class="mb-3">
    <label class="form-label">Stock</label>
    <input class="form-control" name="stock" value="{{ producto.stock }}">
  </div>
  <div class="mb-3">
    <label class="form-label">Categoría</label>
    <input class="form-control" name="categoria" value="{{ producto.categoria }}">
  </div>
  <div class="mb-3">
    <label class="form-label">Código de barras</label>
    <input class="form-control" name="codigo_barras" value="{{ producto.codigo_barras }}">
  </div>
  <div class="mb-3">
    <label class="form-label">URL de imagen</label>
    <input class="form-control" name="imagen_url" value="{{ producto.imagen_url }}">
  </div>
  <button class="btn btn-primary">Actualizar</button>
  <a class="btn btn-secondary" href="{% url 'ver_producto' %}">Cancelar</a>
</form>
{% endblock %}
```

---

#### 📄 `borrar_producto.html`

```html
{% extends "base.html" %}
{% block content %}
<h2>Confirmar eliminación de producto</h2>
<p>¿Seguro que deseas borrar el producto <strong>{{ producto.nombre }}</strong>?</p>
<form method="post">
  {% csrf_token %}
  <button class="btn btn-danger" type="submit">Sí, borrar</button>
  <a class="btn btn-secondary" href="{% url 'ver_producto' %}">Cancelar</a>
</form>
{% endblock %}
```

---

### **8️⃣ No utilizar forms.py**

✅ Ya cumplido: los formularios usan `<form>` manualmente con `request.POST`.

---

### **9️⃣ Agregar rutas en `app_Costco/urls.py`**

Abre `app_Costco/urls.py` y agrega al final:

```python
# --- PRODUCTO ---
path('productos/agregar/', views.agregar_producto, name='agregar_producto'),
path('productos/', views.ver_producto, name='ver_producto'),
path('productos/actualizar/<int:producto_id>/', views.actualizar_producto, name='actualizar_producto'),
path('productos/realizar_actualizacion/<int:producto_id>/', views.realizar_actualizacion_producto, name='realizar_actualizacion_producto'),
path('productos/borrar/<int:producto_id>/', views.borrar_producto, name='borrar_producto'),
```

---

### **🔟 Registrar los modelos en `admin.py` y migrar**

Ya registrado en la primera parte, pero si no lo hiciste:

```python
from django.contrib import admin
from .models import Usuario, Producto, Pedido

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id','nombre','precio','stock','categoria','fecha_creacion')
    search_fields = ('nombre','codigo_barras')
```

Luego:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### **1️⃣1️⃣ Solo trabajar con PRODUCTO**

Deja pendiente el modelo `Pedido` por ahora.

---

### **1️⃣2️⃣ Estilo moderno y colores suaves**

Ya está integrado por `base.html` con Bootstrap.

---

### **1️⃣3️⃣ No validar datos**

No hay validación adicional ni `required`.

---

### **1️⃣4️⃣ Estructura final actualizada**

```
UIII_Costco_0599/
│
├── backend_Costco/
│   ├── settings.py
│   └── urls.py
│
├── app_Costco/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── navbar.html
│   │   ├── footer.html
│   │   ├── inicio.html
│   │   ├── usuario/
│   │   │   ├── agregar_usuario.html
│   │   │   ├── ver_usuario.html
│   │   │   ├── actualizar_usuario.html
│   │   │   └── borrar_usuario.html
│   │   └── producto/
│   │       ├── agregar_producto.html
│   │       ├── ver_producto.html
│   │       ├── actualizar_producto.html
│   │       └── borrar_producto.html
│
└── manage.py
```

---

### **1️⃣5️⃣ Proyecto totalmente funcional**

✅ CRUD completo de `Usuario` y `Producto` operativos.
✅ Navegación actualizada con menú de productos.
✅ Base visual moderna y sencilla.

---

### **1️⃣6️⃣ Ejecutar el servidor en el puerto 8018**

```bash
python manage.py runserver 8018
```

Luego entra a:
👉 `http://127.0.0.1:8018/`
y prueba las rutas:

* `/productos/` → Ver productos
* `/productos/agregar/` → Agregar producto

---

¿Deseas que te prepare la **tercera parte (CRUD del modelo Pedido con relación Usuario–Producto)** de la misma manera (paso a paso + código completo)?
