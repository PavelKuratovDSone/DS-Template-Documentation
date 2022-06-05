Engine.Input
============================

Для реализации стандартного инпута необходимо реализовать следующие интерфейсы

``IBeginDrag`` - для информации об начале ипута

``IDrag`` - для информации об текущим инпуте

``IEndDrag`` - для информации об окончании инпута

``IClick`` - для информации о клике

Все работает по принципу ивентов. Так что предельно важно какой интерфейс вы выбираете - от этого будет зависить когда
вы будете получать новую информацию об инпуте.

BeginDrag
""""""""""""""""""""""""""""

.. code-block:: csharp
     
   using Engine.Input;
   public class DragExample : IBeginDrag
   {
        protected void OnEnable()
        {
            InputEvents.BeginDrag.Subscribe(this);
        }
        protected void OnDisable()
        {
            InputEvents.BeginDrag.Unsubscribe(this);
        }
        private void OnBeginDrag(InputInfo data)
        {
             //data.currentPosition - возвращает Vector3(по экрану) текущее положение пальца
             //data.daltaDrag - возвращает Vector3(по экрану) растояние между началом и текущей
             //data.lengthDrag - возвращает float(по экрану) растояние между началом и текущей
             //data.lastDaltaDrag - возвращает Vector3(по экрану) текущее положение пальца
             //data.initPoint - возвращает Vector3(по экрану) растояние между последней сменой направления и текущей
             //data.lastPosition - возвращает Vector3(по экрану) последнее положение пальца
        }
                
   }

Drag
""""""""""""""""""""""""""""

.. code-block:: csharp
     
   using Engine.Input;
   public class DragExample : IDrag
   {
        protected void OnEnable()
        {
            InputEvents.Drag.Subscribe(this);
        }
        protected void OnDisable()
        {
            InputEvents.Drag.Unsubscribe(this);
        }
        private void OnDrag(InputInfo data)
        {
             //data.currentPosition - возвращает Vector3(по экрану) текущее положение пальца
             //data.daltaDrag - возвращает Vector3(по экрану) растояние между началом и текущей
             //data.lengthDrag - возвращает float(по экрану) растояние между началом и текущей
             //data.lastDaltaDrag - возвращает Vector3(по экрану) текущее положение пальца
             //data.initPoint - возвращает Vector3(по экрану) растояние между последней сменой направления и текущей
             //data.lastPosition - возвращает Vector3(по экрану) последнее положение пальца
        }
                
   }

EndDrag
""""""""""""""""""""""""""""

.. code-block:: csharp
     
   using Engine.Input;
   public class DragExample : IEndDrag
   {
        protected void OnEnable()
        {
            InputEvents.EndDrag.Subscribe(this);
        }
        protected void OnDisable()
        {
            InputEvents.EndDrag.Unsubscribe(this);
        }
        private void OnEndDrag(InputInfo data)
        {
             //data.currentPosition - возвращает Vector3(по экрану) текущее положение пальца
             //data.daltaDrag - возвращает Vector3(по экрану) растояние между началом и текущей
             //data.lengthDrag - возвращает float(по экрану) растояние между началом и текущей
             //data.lastDaltaDrag - возвращает Vector3(по экрану) текущее положение пальца
             //data.initPoint - возвращает Vector3(по экрану) растояние между последней сменой направления и текущей
             //data.lastPosition - возвращает Vector3(по экрану) последнее положение пальца
        }
                
   }

Click
""""""""""""""""""""""""""""

.. code-block:: csharp
     
   using Engine.Input;
   public class DragExample : IClick
   {
        protected void OnEnable()
        {
            InputEvents.Click.Subscribe(this);
        }
        protected void OnDisable()
        {
            InputEvents.Click.Unsubscribe(this);
        }
        private void OnClick(InputInfo data)
        {
             //data.currentPosition - возвращает Vector3(по экрану) текущее положение пальца
             //data.daltaDrag - возвращает Vector3(по экрану) растояние между началом и текущей
             //data.lengthDrag - возвращает float(по экрану) растояние между началом и текущей
             //data.lastDaltaDrag - возвращает Vector3(по экрану) текущее положение пальца
             //data.initPoint - возвращает Vector3(по экрану) растояние между последней сменой направления и текущей
             //data.lastPosition - возвращает Vector3(по экрану) последнее положение пальца
        }
                
   }





