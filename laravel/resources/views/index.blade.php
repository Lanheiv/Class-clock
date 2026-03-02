<x-layout>
  <div id="container" class="px-4 pt-4">
    <div class="grid grid-cols-2 grid-rows-6 gap-4 text-center min-h-[80vh]">
        <div class="p-2 col-span-2 row-span-1 rounded-lg border border-gray-200 shadow-md content-center">
            <p class="text-xl font-bold text-gray-800">Vidzemes Tehnoloģiju un Dizaina Tehnikuma Stundu Saraksts </p>
        </div>
        <div class="p-4 pt-0 col-span-2 row-span-5 rounded-lg border border-gray-200 shadow-md">
            <div class="flex items-center border border-gray-200 border-t-0 rounded-b-lg shadow-md h-12">
                <div class="pl-4">
                    <form id="form_select" class="max-w-sm mx-auto">
                        <label for="underline_select_gruop" class="sr-only">Underline select</label>
                        <select id="underline_select_gruop" class="block py-1 ps-0 w-full text-sm text-body bg-transparent border-0 border-b-2 border-default-medium appearance-none focus:outline-none focus:ring-0 focus:border-brand peer">
                        </select>
                    </form>
                </div>
            </div>
            <div id="tabel" class="pt-4">
                <x-table />
            </div>
        </div>
    </div>
  </div>
</x-layout>