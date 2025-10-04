# Обновленная, профессиональная версия MYneuron.py

class Neuron:
    """
    Класс, моделирующий один нейрон по модели Leaky Integrate-and-Fire (LIF).

    Атрибуты:
    ----------
    V_rest : float
        Потенциал покоя мембраны в мВ.
    V_thresh : float
        Порог срабатывания для генерации спайка в мВ.
    V_reset : float
        Потенциал сброса после спайка в мВ.
    R : float
        Сопротивление мембраны в МОм.
    C : float
        Емкость мембраны в нФ.
    V : float
        Текущий мембранный потенциал в мВ.
    """

    def __init__(self):
        """Инициализирует нейрон с параметрами по умолчанию."""
        self.V_rest: float = -70.0
        self.V_thresh: float = -55.0
        self.V_reset: float = -75.0
        self.R: float = 10.0
        self.C: float = 1.0
        self.V: float = self.V_rest

    def update(self, dt: float, I: float) -> bool:
        """
        Обновляет состояние нейрона за один временной шаг.

        Параметры:
        -----------
        dt : float
            Временной шаг симуляции в мс.
        I : float
            Входной ток в нА.

        Возвращает:
        -----------
        bool
            True, если нейрон сгенерировал спайк на этом шаге, иначе False.
        """
        dV = ((self.V_rest - self.V) / self.R + I) / self.C * dt
        self.V += dV  # (self.V += dV) - это короткая запись для (self.V = self.V + dV)

        if self.V >= self.V_thresh:
            self.V = self.V_reset
            return True

        return False


