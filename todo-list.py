class TodoList:
    def __init__(self, filename='todo_list.txt'):
        self.filename = filename
        self.todos = self.load_todos()

    def load_todos(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                return file.read().splitlines()
        except FileNotFoundError:
            return []

    def save_todos(self):
        with open(self.filename, 'w', encoding='utf-8') as file:
            for todo in self.todos:
                file.write(f"{todo}\n")

    def add(self, task):
        self.todos.append(task)
        self.save_todos()

    def remove(self, index):
        if 0 <= index < len(self.todos):
            del self.todos[index]
            self.save_todos()
        else:
            print("無効なインデックスです。")

    def display(self):
        for index, todo in enumerate(self.todos, start=1):
            print(f"{index}. {todo}")

def main():
    todo_list = TodoList()
    while True:
        print("\nTODOリスト管理")
        print("1. TODOを表示")
        print("2. TODOを追加")
        print("3. TODOを削除")
        print("4. 終了")
        choice = input("選択: ")

        if choice == '1':
            todo_list.display()
        elif choice == '2':
            task = input("追加するTODO: ")
            todo_list.add(task)
            print("TODOが追加されました。")
        elif choice == '3':
            index = int(input("削除するTODOの番号: ")) - 1
            todo_list.remove(index)
            print("TODOが削除されました。")
        elif choice == '4':
            print("プログラムを終了します。")
            break
        else:
            print("無効な選択です。")

if __name__ == "__main__":
    main()