Engine.Coin
============================

По умолчанию контейнер с монетами уже существует. Для того чтобы получить доступ к информации о монетах
необходимо прокинуть зависимости.

Пример:

.. code-block:: sharp
    public class AddCoinsExample
    {
        public ICoinsData coinsData;
        void OnEnable()
        {
            coinsData = Engine.DI.DIContainer.GetAsSingle<ICoinsData>();
            coinsData.onUpdate += OnCoinsUpdated;
        }
        void OnEnable()
        {
            coinsData.onUpdate -= OnCoinsUpdated;      
        }
        private void OnCoinsUpdated(ParametersUpdate obj)
        {
            Debug.Log("Coins is updated...");
        }
    }
