<template>
    <nav class="bg-blue-500 p-2 mt-0 w-full">
        <div class="container mx-auto flex flex-wrap items-center">
            <div class="flex w-full md:w-1/2 justify-center md:justify-start text-white font-extrabold">
                <a class="text-white no-underline hover:text-white hover:no-underline" href="#">
                    <span class="text-2xl pl-2">Library App</span>
                </a>
            </div>
            <div class="flex w-full pt-2 content-center justify-between md:w-1/2 md:justify-end">
                <ul class="list-reset flex justify-between flex-1 md:flex-none items-center">
                    <li class="mr-3">
                        <router-link to="/books" class="inline-block py-2 px-4 text-white no-underline">Books</router-link>
                    </li>
                    <li class="mr-3">
                        <router-link to="/members"
                            class="inline-block py-2 px-4 text-white no-underline">Members</router-link>
                    </li>
                    <li class="mr-3">
                        <a class="inline-block text-blue-300 no-underline hover:text-gray-800 hover:text-underline py-2 px-4"
                            href="#">Transactions</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
</template>
