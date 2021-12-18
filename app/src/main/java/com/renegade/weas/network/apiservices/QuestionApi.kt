package com.renegade.weas.network.apiservices

import com.renegade.weas.network.requestbody.QuestionBody
import com.renegade.weas.network.response.questionresponse.QuestionResponse
import retrofit2.Response
import retrofit2.http.Body
import retrofit2.http.POST

interface QuestionApi {
    @POST("api/v1/question/")
    suspend fun getFirstQuestion(): Response<QuestionResponse>

    @POST("api/v1/question/")
    suspend fun getNextQuestion(@Body questionBody: QuestionBody): Response<QuestionResponse>
}