Engine.Coin
============================

По умолчанию контейнер с монетами уже существует. Для того чтобы получить доступ к информации о монетах
необходимо прокинуть зависимости.

**Пример:**

.. code-block:: csharp

    public class CoinsExample
    {
        public ICoinsData coinsData;
        void OnEnable()
        {
            coinsData = Engine.DI.DIContainer.GetAsSingle<ICoinsData>();
        }
    }

Далее можно проводить различные операции с балансом

**Получить информацию о балансе**

.. code-block:: csharp

    coinsData.totalCoins
    
**Прибавить к балансу**

.. code-block:: csharp

    int amount=100;
    coinsData.AddCoins(amount);
    
**Отнять от баланса**

.. code-block:: csharp

    int amount=100;
    coinsData.RemoveCoins(amount); 
    
**Подписаться и отписаться на изменения баланса**
 
 .. code-block:: csharp
 
     public class CoinsExample
         {
             public ICoinsData coinsData;
             void OnEnable()
             {
                 coinsData = Engine.DI.DIContainer.GetAsSingle<ICoinsData>();
                 coinsData.onUpdate += OnCoinsUpdated;
             }
             void OnDisable()
             {
                 coinsData.onUpdate -= OnCoinsUpdated;      
             }
             private void OnCoinsUpdated(ParametersUpdate obj)
             {
                 Debug.Log("Coins is updated...");
                 //obj.amount - возвращает кол-во на которое произошло изменение
                 //obj.operation - возвращает Engine.Coin.OperationType {Add или Minus}
                 //obj.total - возвращает итоговое кол-во монет
             }
         }   

