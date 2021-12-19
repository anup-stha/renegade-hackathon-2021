package com.renegade.weas.ui.addalert

import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.recyclerview.widget.DiffUtil
import androidx.recyclerview.widget.ListAdapter
import androidx.recyclerview.widget.RecyclerView
import com.renegade.weas.R
import com.renegade.weas.network.requestbody.AlertBody

class PersonnelListRVA : ListAdapter<AlertBody, PersonnelListRVA.Holder>(PersonnelDiffCallback()) {
    class Holder(itemView: View) : RecyclerView.ViewHolder(itemView) {
        val nameTV: TextView = itemView.findViewById(R.id.name)
        val relationTV: TextView = itemView.findViewById(R.id.relationship)
        val emailTV: TextView = itemView.findViewById(R.id.email)
        val phoneTV: TextView = itemView.findViewById(R.id.phone)

    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): Holder {
        return Holder(
            LayoutInflater.from(parent.context).inflate(
                R.layout.alert_grp_list_layout, parent, false
            )
        )
    }

    override fun onBindViewHolder(holder: Holder, position: Int) {
        val item = getItem(position)
        holder.nameTV.text = item.name
        holder.emailTV.text = item.email
        holder.phoneTV.text = item.phone
        holder.relationTV.text = item.relationShip
    }
}

class PersonnelDiffCallback : DiffUtil.ItemCallback<AlertBody>() {
    override fun areItemsTheSame(oldItem: AlertBody, newItem: AlertBody): Boolean {
        return oldItem.id == newItem.id
    }

    override fun areContentsTheSame(oldItem: AlertBody, newItem: AlertBody): Boolean {
        return (oldItem.id == newItem.id
                && oldItem.email == newItem.email
                && oldItem.phone == newItem.phone
                && oldItem.relationShip == newItem.relationShip
                && oldItem.name == newItem.name)
    }

}