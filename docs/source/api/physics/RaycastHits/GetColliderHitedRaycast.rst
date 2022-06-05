Physic.RaycastHits.GetColliderHitedRaycast
============================

.. code-block:: csharp
    
    using Engine.Input;
    using UnityEngine;
    public class GetColliderHitedRaycastExample : MonoBehaviour
    {
            private void Update()
            {
                if (ControllerInputs.OnMouse(MouseStatue.Down))
                {
                    
                        Debug.Log(Physic.RaycastHits.GetColliderHitedRaycast<BoxCollider>(Camera.main, UnityEngine.Input.mousePosition));
                }
            }
    }
