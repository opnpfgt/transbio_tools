# Transbio Tools

Transbio Tools — это набор модулей для работы с биологическими последовательностями ДНК и РНК и реализации процессов центральной догмы молекулярной биологии, а также для фильтрации данных в формате FASTQ.

## Структура проекта

- module_for_filter_fastq.py         # Модуль для фильтрации данных FASTQ

- module_for_dna_rna_tools.py        # Модуль для работы с ДНК и РНК

- fastq_filtrator.py                 # Главный модуль для запуска инструментов обработки ДНК и РНК



## Модули

### 1. `module_for_filter_fastq.py`

Этот модуль содержит функции для вычисления GC-содержания и среднего качества последовательностей.

- **Функции:**
  - `gc_bound(seq: str) -> float`: Вычисляет процентное содержание G и C в последовательности.
  - `avg_quality(quality: str) -> float`: Вычисляет среднее качество последовательности.

### 2. `module_for_dna_rna_tools.py`

Этот модуль предоставляет функции для работы с ДНК и РНК, включая получение комплементарной последовательности, транскрипцию и обратную транскрипцию.

- **Функции:**
  - `get_na_type(seq: str) -> str`: Определяет тип нуклеиновой кислоты (ДНК или РНК) или сообщает об ошибке.
  - `complement(seq: str) -> str`: Возвращает комплементарную последовательность.
  - `transcribe(dna_seq: str) -> str`: Транскрибирует ДНК в РНК.
  - `reverse_transcribe(rna_seq: str) -> str`: Обратная транскрипция РНК в ДНК.
  - `reverse(seq: str) -> str`: Возвращает обратную последовательность.
  - `reverse_complement(seq: str) -> str`: Возвращает обратную комплементарную последовательность.

### 3. `transbio_tool.py`

Этот модуль объединяет функции из предыдущих модулей и предоставляет интерфейс для обработки последовательностей ДНК и РНК. 

- **Функция:**
  - `run_dna_rna_tools(*args)`: Запускает указанные процедуры (транскрипция, комплементация и т.д.) для переданных последовательностей.
  - `filter_fastq(seqs: Dict[str, Tuple[str, str]], gc_bounds: Union[int, float, tuple], length_bounds: Union[int, float, tuple], quality_threshold: Union[int, float]) -> Dict[str, Tuple[str, str]]`: Фильтрует данные в формате FASTQ по заданным критериям (GC-содержание, длина, качество).

## Установка

Для использования модулей просто скопируйте папку `transbio_tools` в ваш проект. Убедитесь, что все зависимости установлены (если есть).

## Примеры использования

### Фильтрация FASTQ

```python
from transbio_tools.fastq_filtrator import filter_fastq

seqs = {
    '@SRX079801': (
        'ACAGCAACATAAACATGATGGGATGGCGTAAGCCCCCGAGATATCAGTTTACCCAGGATAAGAGATTAAATTATGAGCAACATTATTAA',
        'FGGGFGGGFGGGFGDFGCEBB@CCDFDDFFFFBFFGFGEFDFFFF;D@DD>C@DDGGGDFGDGG?GFGFEGFGGEF@FDGGGFGFBGGD'
    )
}

filtered_sequences = filter_fastq(seqs, gc_bounds=(30, 60), length_bounds=(0, 100), quality_threshold=20)
print(filtered_sequences)

Работа с ДНК и РНК

from transbio_tools.modules.module_for_dna_rna_tools import transcribe, complement

dna_seq = "ATGC"
rna_seq = transcribe(dna_seq)
complement_seq = complement(dna_seq)

print(f"Транскрибированная последовательность: {rna_seq}")
print(f"Комплементарная последовательность: {complement_seq}")
