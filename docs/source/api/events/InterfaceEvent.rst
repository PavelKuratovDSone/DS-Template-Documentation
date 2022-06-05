Engine.Events.InterfaceEvent
============================

Позволяет создавать в роли ивента целый класс или струтуру.
Формально это система обратных ивентов. Когда мы точно знаем на момент вызова ивента что будет выполнено.

Для начала нужно создать интерфейс с методами которые мы захотим вызывать по ивенту.

.. code-block:: csharp
    
    public interface IExecuteExample
    {
            void Execute();
            
    }
    
Далее нужно реализовать класс\структуру и методы которые мы будем выполнять по ивенту.

.. code-block:: csharp
    
    public class ExecuteExample : IExecuteExample
    {
            public void Execute()
            {
                Debug.Log("Is Executed...");
            }
    }
    
Теперь необходимо создать место вызова ивента. 
Поскольку мы используем для примера механику с интерфейсами - то и использовать будем ``InterfaceEvent``.

.. code-block:: csharp

    public class InterfaceEventExample : MonoBehaviour
    {
            //Создаем экземляр ивента
            public InterfaceEvent<IExecuteExample> executions = new InterfaceEvent<IExecuteExample>();
    
            private void OnEnable()
            {
                //Подписываем наш ивент и указываем какой класс\структуру хотим выполнить.
                executions.Subscribe(new ExecuteExample());
            }
    
            private void OnDisable()
            {
                executions.Unsubscribe(new ExecuteExample());
            }
            
            //Вызываем срабатывание нашего ивента и указываем какой метод выполнить.
            [NaughtyAttributes.Button("Execute")]
            public void Execute()
            {     
                executions.Invoke(item => item.Execute());
            }
    }
