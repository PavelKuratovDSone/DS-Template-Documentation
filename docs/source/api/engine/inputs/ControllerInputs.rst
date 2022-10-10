Engine.Input.ControllerInputs
============================

Работа с мышкой

Engine.Input.ControllerInputs.OnMouse(MouseStatue)
""""""""""""""""""""""""""""
Возвращает ``bool``.

Engine.Input.ControllerInputs.GetMouseState()
""""""""""""""""""""""""""""
Возвращает ``MouseStatue``.

Engine.Input.ControllerInputs.s_EnableInputs
""""""""""""""""""""""""""""
Возвращает ``bool`` включен ли input.

Engine.Input.ControllerInputs.IsRaycastedUI
""""""""""""""""""""""""""""
Возвращает ``bool`` было ли пересечение с каким либо объектом рейкастом.


MouseStatue
""""""""""""""""""""""""""""

.. table:: ``MouseStatue``

    +------------------------+------------+----------+----------+
    | ``MouseStatue``        |             Значение             |
    |                        |                                  |
    +========================+============+==========+==========+
    | ``MouseStatue.Down``   |  Возвращается когда левая кнопка |
    |                        |  мышки зажата.                   |
    +------------------------+------------+----------+----------+
    | ``MouseStatue.Idle``   |  ?                               |
    +------------------------+------------+---------------------+
    | ``MouseStatue.Non``    |  ?                               |
    +------------------------+----------------------------------+
    | ``MouseStatue.Up``     |  Возвращается когда левая кнопка |
    |                        |  мышки была отжата.              |
    +------------------------+------------+---------------------+


Пример:

.. code-block:: csharp

    using Engine.Input;
    using UnityEngine;
    
    
    public class ControllerInputsExample : MonoBehaviour
    {
         private void Update()
         {
                if (ControllerInputs.OnMouse(MouseStatue.Down))
                {
                    Debug.Log("Мышь нажата\зажата");
                }
            }
    }
     